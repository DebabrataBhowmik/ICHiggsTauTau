from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.workArea='July08_MC_74X'
#config.General.requestName = 'May13_MC'
config.section_('JobType')
config.JobType.psetName = '/afs/cern.ch/work/a/adewit/private/CMSSW_7_4_5/src/UserCode/ICHiggsTauTau/test/miniaod_cfg_new_recipes_74.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['EventTree.root']
config.JobType.pyCfgParams = ['release=74XMINIAOD','isData=0','isNLO=0']
config.section_('Data')
#config.Data.inputDataset = 'DUMMY'
config.Data.unitsPerJob = 30000 
config.Data.splitting = 'EventAwareLumiBased'
config.Data.publication = False
config.Data.outLFNDirBase='/store/user/adewit/July08_MC_74X/'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_UK_London_IC', 'T2_CH_CERN', 'T2_FR_GRIF_LLR', 'T2_UK_SGrid_Bristol', 'T3_US_FNALLPC', 'T2_DE_DESY', 'T2_IT_Bari', 'T2_BE_IIHE', 'T2_US_UCSD', 'T2_US_MIT', 'T2_IT_Pisa', 'T2_US_Wisconsin', 'T2_US_Florida', 'T2_IT_Rome', 'T2_RU_JINR']
config.Site.storageSite = 'T2_UK_London_IC'

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException, hte:
            print hte.headers

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    tasks=list()

    tasks.append(('SUSYGluGluToHToTauTau_M-500','/SUSYGluGluToHToTauTau_M-500_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-160','/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-130','/SUSYGluGluToHToTauTau_M-130_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'))
#    tasks.append(('SUSYGluGluToBBHToTauTau_M-500','/SUSYGluGluToBBHToTauTau_M-500_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'))
#    tasks.append(('SUSYGluGluToBBHToTauTau_M-160','/SUSYGluGluToBBHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM'))
    tasks.append(('WWinclusive','/WW_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'))
    tasks.append(('WZinclusive','/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'))
    tasks.append(('ZZinclusive','/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/MINIAODSIM'))
    tasks.append(('QCDFlat','/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/RunIISpring15DR74-Asympt25nsRaw_MCRUN2_74_V9-v3/MINIAODSIM'))
    tasks.append(('QCDMuEnr','/QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'))
    tasks.append(('T-tW','/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'))
    tasks.append(('Tbar-tW','/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'))
    tasks.append(('TT','/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM'))

    for task in tasks:
        print task[0]
        config.General.requestName = task[0]
        config.Data.inputDataset = task[1]
        submit(config)


