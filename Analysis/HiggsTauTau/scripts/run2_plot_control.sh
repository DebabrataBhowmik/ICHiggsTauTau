./bin/HiggsTauTauPlot5 --cfg=scripts/new_plot_sm_2014.cfg --channel=et --set_alias="sel:mt_1<30."   --method=8 --cat="inclusive" --var="pt_1(25,0,100)"  --x_axis_label="Electron p_{T} [GeV]" --datacard="inclusive"   --background_scheme="et_no_qcd" --extra_pad=0.2 --verbosity=0
./bin/HiggsTauTauPlot5 --cfg=scripts/new_plot_sm_2014.cfg --channel=et --set_alias="sel:mt_1<30."   --method=8 --cat="1jet" --var="pt_1(25,0,100)"   --x_axis_label="Electron p_{T} [GeV]" --datacard="1jet"   --background_scheme="et_no_qcd" --extra_pad=0.2 --verbosity=0
./bin/HiggsTauTauPlot5 --cfg=scripts/new_plot_sm_2014.cfg --channel=et --set_alias="sel:mt_1<30."   --method=8 --cat="vbf" --var="pt_1(25,0,100)"   --x_axis_label="Electron p_{T} [GeV]" --datacard="vbf"   --background_scheme="et_no_qcd" --extra_pad=0.2 --verbosity=0