from WMCore.Configuration import Configuration
from multiprocessing import Process
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.workArea='Aug14_MC_80X'
config.section_('JobType')
config.JobType.psetName = 'higgstautau_cfg_80X_Nov17.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['EventTree.root']
pyCfgParams = ['release=80XMINIAOD','isData=0','globalTag=80X_mcRun2_asymptotic_2016_TrancheIV_v8','isReHLT=1','LHEWeights=True']
config.section_('Data')
config.Data.unitsPerJob = 100000
config.Data.splitting = 'EventAwareLumiBased'
config.Data.publication = False
#config.Data.ignoreLocality= True
config.Data.outLFNDirBase='/store/user/dwinterb/Aug14_MC_80X/'
config.section_('User')
config.section_('Site')
#config.Site.whitelist = ['T1_*', 'T2_*', 'T3_*']
config.Site.storageSite = 'T2_UK_London_IC'
config.JobType.allowUndistributedCMSSW = True

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

    #tasks.append(('GluGluHToTauTau_M125_NNLOPS','/GluGluHToGG_M-125_13TeV_powheg_MINLO_NNLOPS_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/MINIAODSIM'))
    tasks.append(('GluGluToHToTauTau_M125_amcatnloFXFX','/GluGluToHToTauTau_M125_13TeV_amcatnloFXFX_pythia8_2016-GEN/dwinterb-GluGluToHToTauTau_M125_13TeV_amcatnloFXFX_pythia8_2016-MiniAOD-28028af67189b3de7224b79195bd0e1d/USER'))
    tasks.append(('GluGluToPseudoscalarHToTauTau_M125_amcatnloFXFX','/GluGluToPseudoscalarHToTauTau_M125_13TeV_amcatnloFXFX_pythia8_2016-GEN/dwinterb-GluGluToPseudoscalarHToTauTau_M125_13TeV_amcatnloFXFX_pythia8_2016-MiniAOD-28028af67189b3de7224b79195bd0e1d/USER'))
    tasks.append(('GluGluToMaxmixHToTauTau_M125_amcatnloFXFX','/GluGluToMaxmixHToTauTau_M125_13TeV_amcatnloFXFX_pythia8_2016-GEN/dwinterb-GluGluToMaxmixHToTauTau_M125_13TeV_amcatnloFXFX_pythia8_2016-MiniAOD-28028af67189b3de7224b79195bd0e1d/USER'))

    #tasks.append(('GluGluToMaxmixHToTauTauPlusTwoJets_M125_amcatnloFXFX','/GluGluToMaxmixHToTauTauPlusTwoJets_M125_13TeV_amcatnloFXFX_pythia8_2016-GEN/dwinterb-GluGluToMaxmixHToTauTauPlusTwoJets_M125_13TeV_amcatnloFXFX_pythia8_2016-MiniAOD-28028af67189b3de7224b79195bd0e1d/USER'))

    #tasks.append(('GluGluToHToTauTauPlusTwoJets_M125_amcatnloFXFX','/GluGluToHToTauTauPlusTwoJets_M125_13TeV_amcatnloFXFX_pythia8_2016-GEN/dwinterb-GluGluToHToTauTauPlusTwoJets_M125_13TeV_amcatnloFXFX_pythia8_2016-MiniAOD-28028af67189b3de7224b79195bd0e1d/USER'))

    #tasks.append(('GluGluToPseudoscalarHToTauTauPlusTwoJets_M125_amcatnloFXFX', '/GluGluToPseudoscalarHToTauTauPlusTwoJets_M125_13TeV_amcatnloFXFX_pythia8_2016-GEN/dwinterb-GluGluToPseudoscalarHToTauTauPlusTwoJets_M125_13TeV_amcatnloFXFX_pythia8_2016-MiniAOD-28028af67189b3de7224b79195bd0e1d/USER'))

    for task in tasks:
        print task[0]
        config.General.requestName = task[0]
        config.Data.inputDataset = task[1]

        if 'amcatnloFXFX' in task[0]: config.Data.inputDBS = 'phys03'
        else: config.Data.inputDBS = 'global'            
        if 'NNLOPS' in task[0]:
          config.JobType.pyCfgParams = pyCfgParams+['LHETag=source']
        else:
          config.JobType.pyCfgParams = pyCfgParams+['doHT=1','includenpNLO=True']
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()



