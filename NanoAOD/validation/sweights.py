import os
import ROOT
from datetime import datetime
from ROOT import TChain, TFile
from time import sleep
import math 

def make_dataset(tree, name, mass_var, other_vars, cuts=""):

    ### Build the dataset
    
    var_set = ROOT.RooArgSet()
    for var in other_vars:
        var_set.add(var)
    var_set.add(mass_var)

    data = ROOT.RooDataSet(name, "", var_set, ROOT.RooFit.Import(tree))
    if cuts != "":
        data = data.reduce(cuts)

    # data.Print("V")
    print "Input tree has ", tree.GetEntries(), "entries. The derived dataset has ", data.sumEntries()

    return data

def get_workspace_with_weights_for_jpsik(tree, name, mass_var, other_vars, cuts=""):
    data = make_dataset(tree, name, mass_var, other_vars, cuts)

    ### Build model
    
    sigma = ROOT.RooRealVar("sigma", "sigma", 0.005, 0.001, 0.02)
    mean  = ROOT.RooRealVar("mean", "mean", 5.28, 5.25, 5.30)
    sig   = ROOT.RooGaussian("gaus", "", mass_var, mean, sigma)

    a0    = ROOT.RooRealVar("a0", "a0", 0.0, -1., 1.)
    bkg   = ROOT.RooChebychev("bkg", "Background", mass_var, ROOT.RooArgList(a0))

    Nsig  = ROOT.RooRealVar("Nsig", "Nsig", 1000, 0, 1e9)
    Nbkg  = ROOT.RooRealVar("Nbkg", "Nbkg", 0, 0, 1e9)
    model = ROOT.RooAddPdf("model", "", ROOT.RooArgList(sig,bkg), ROOT.RooArgList(Nsig,Nbkg))

    ### Fit
    
    model.fitTo(data,  ROOT.RooFit.Extended(ROOT.kTRUE), ROOT.RooFit.Minos(ROOT.kFALSE))

    ### Compute sWeights
    
    ROOT.RooStats.SPlot("sData", "An SPlot", data, model, ROOT.RooArgList(Nsig,Nbkg))

    ws = ROOT.RooWorkspace("ws","")
    getattr(ws,'import')(data)
    getattr(ws,'import')(model)
    # ws.Import(data)
    # ws.Import(model)

    # data.Print("V")
    
    return ws

if __name__ == '__main__':
    tree = ROOT.TChain("mva")
    # tree.Add("/eos/cms/store/group/phys_bphys/bmm/bmm5/PostProcessing/FlatNtuples/512/bmm_mva_jpsik/Charmonium+Run2018D-PromptReco-v2+MINIAOD/*.root")
    tree.Add("/eos/cms/store/group/phys_bphys/bmm/bmm5/PostProcessing/FlatNtuples/512/bmm_mva_jpsik/Charmonium+Run2018D-PromptReco-v2+MINIAOD/0aa7acf37201fe007dfaa71f4cfb9eac.root")
    # tree.Add("/eos/cms/store/group/phys_bphys/bmm/bmm5/PostProcessing/FlatNtuples/515/bmm_mva_jpsik/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCUEP8M1_13TeV-pythia8-evtgen+RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2+MINIAODSIM/2b4896bfe4572b22d81bc7e25f9666eb.root")

    mass = ROOT.RooRealVar("mm_kin_mass", "", 5.15, 5.45)
    vars = [
        ROOT.RooRealVar("mm_kin_alpha", "", 0, 0.2),
    ]

    ws = get_workspace_with_weights_for_jpsik(tree, 'data', mass, vars)
    data = ws.data("data")
    model = ws.pdf("model")
    alpha = ws.var("mm_kin_alpha")
    mass = ws.var("mm_kin_mass")
    
    c1 = ROOT.TCanvas("c1","c1", 1200, 400)
    c1.Divide(3,1)
    
    hsub = ROOT.RooAbsData.createHistogram(data, 'all', alpha, ROOT.RooFit.Binning(20))
    c1.cd(1)
    hsub.Draw()
    
    frame = mass.frame()
    data.plotOn(frame)
    model.plotOn(frame)
    # # model.plotOn(frame, ROOT.RooFit.Components(bkg), ROOT.RooFit.LineStyle(ROOT.kDashed))

    model.paramOn(frame, ROOT.RooFit.Layout(0.6, 0.85, 0.85))
    # # model->paramOn(frame, Layout(0.55));
    frame.getAttText().SetTextSize(0.02)
    c1.cd(2)
    frame.Draw()

    dataw_sig = ROOT.RooDataSet(data.GetName(), data.GetTitle(), data, data.get(), "", "Nsig_sw")

    hsub = ROOT.RooAbsData.createHistogram( dataw_sig, 'sig', alpha, ROOT.RooFit.Binning(20))

    c1.cd(3)
    hsub.Draw()
    c1.Update()
    raw_input("Press enter to continue")
    # https://sft.its.cern.ch/jira/si/jira.issueviews:issue-html/ROOT-9890/ROOT-9890.html
    ws.Delete() 
