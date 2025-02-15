# Changelog

## New developments

## [NanoAODv8-V02] - 2021/07/03
### Added
	- Trigger prescale for selected set of HLT triggers
	- GenFilterInfo in LuminosityBlocks to compute proper event yield normalization

### Fixed
	- GenInfo extraction for JpsiK
	- Added exception handling for bad fits

## [NanoAODv8-V01] - 2021/05/26
	- Ultra Legacy equivalent of NanoAODv6-V17. Requires CMSSW_10_6_19_patch2

## [NanoAODv6-V17] - 2021/05/10

### Fixed
	- Added protection from getting NaN for pointing angle in a special case

## [NanoAODv6-V16] - 2021/05/07

### Fixed
	- Removed confusing pointing angle definitions and renamed some of them
	- Added protection from NaN in impact parameter calculation

### Added
	- new soft muon MVA
	- uncertainty calculation for pointing angle
	- reorganized/modified some core code - bugs are possible

## [NanoAODv6-V15] - 2021/04/10

### Fixed
	- Fixed bug in JpsiKK code
	- Increase DsToPhiPi mass windows

## [NanoAODv6-V14] - 2021/04/02

### Fixed
	- use only a single thread in XGBooster

### Added
	- muon id inputs for new MVA id
	- DsToPhiPiToKKPi control samples
	- expanded JpsiK to mmK including Psi(2S)K
	- better postprocessing

## [NanoAODv6-V13] - 2021/01/05

### Fixed
	- catch std::exceptions during fitting and mark fit as invalid

## [NanoAODv6-V12] - 2020/12/08

### Fixed
	- bug fix in Lambda reconstruction

## [NanoAODv6-V11] - 2020/12/04

### Added
	- V0 impact parameter info
	- extra impact parameter info for B candidates

### Fixed
	- enforce PF candidate mass hypothesis in V0 candidates

## [NanoAODv6-V10] - 2020/11/27

### Added
	- Added D0ToKPi, LambdaToPPi and PhiToKK for muon fake studies
	- Added track impact parameter for V0

### Modified
	- MC matching for V0 is modified to inmprobe matching efficiency

## [NanoAODv6-V09] - 2020/08/21

### Fixed
	- Fixed bug in MuonCand build from a hadron (the track reference could be wrong)

## [NanoAODv6-V08] - 2020/08/06

### Added
	- Injected hadrons from relevant exclusive decays into good muon candidates to study muon fakes. This may break some old code since muon index for hadron is a negative number and cannot be used to reference a muon unless it was reconstructed as a muon
	- Added gen summary for all relevant exclusive backgrounds
	- Added a few variables
### Modified
	- Redesinged genbmm block. It is not compatible with the old code.
	- Improved gen matching (adde extra information and started using packed candidates)
### Fixed
	- Fixed bug in matching tracks to ignore

## [NanoAODv6-V07] - 2020/05/26

### Added
	- Recompute soft muon MVA

## [NanoAODv6-V06] - 2020/05/15

### Added
	- Bmm emulation with BtoJpsiK events
	- skimming tools
	- KsToPiPi reconstruction for muon fake studies
	- dimuon vertexing with pointing constrain (kinpc)
	- XGBoost is integrated in NanoAOD code to produce ntuple with new MVA centrally
	- Generator level filter for Bmm signature to effectively select relevant QCD events
	- MC production config files

## [NanoAODv6-V05] - 2020/03/16

### Fixed
	- Fixed bug in generator level information extraction critical for efficiency studies

## [NanoAODv6-V04] - 2020/03/06

### Added
	- kk mass for BsToJpsiPhi
	- Bmm gen event level information for efficiency studies
	- event classification based on the production type
	- decay time in 3D and 2D
	- gen decay time
	- added some missing kinematic variables

### Fixed
	- fixed refitted daughter information
