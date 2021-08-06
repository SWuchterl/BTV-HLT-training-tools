global_branches = ['jet_pt', 'jet_eta',
'nCpfcand','nNpfcand',
'nsv','npv',
'TagVarCSV_trackSumJetEtRatio',
'TagVarCSV_trackSumJetDeltaR',
'TagVarCSV_vertexCategory',
'TagVarCSV_trackSip2dValAboveCharm',
'TagVarCSV_trackSip2dSigAboveCharm',
'TagVarCSV_trackSip3dValAboveCharm',
'TagVarCSV_trackSip3dSigAboveCharm',
'TagVarCSV_jetNSelectedTracks',
'TagVarCSV_jetNTracksEtaRel'
]

cpf_branches = ['Cpfcan_BtagPf_trackEtaRel',
'Cpfcan_BtagPf_trackPtRel',
'Cpfcan_BtagPf_trackPPar',
'Cpfcan_BtagPf_trackDeltaR',
'Cpfcan_BtagPf_trackPParRatio',
'Cpfcan_BtagPf_trackSip2dVal',
'Cpfcan_BtagPf_trackSip2dSig',
'Cpfcan_BtagPf_trackSip3dVal',
'Cpfcan_BtagPf_trackSip3dSig',
'Cpfcan_BtagPf_trackJetDistVal',
'Cpfcan_ptrel',
'Cpfcan_drminsv',
'Cpfcan_VTX_ass',
'Cpfcan_puppiw',
'Cpfcan_chi2',
'Cpfcan_quality']
n_cpf = 25

npf_branches = ['Npfcan_ptrel','Npfcan_deltaR','Npfcan_isGamma','Npfcan_HadFrac','Npfcan_drminsv','Npfcan_puppiw']
n_npf = 25

vtx_branches = ['sv_pt','sv_deltaR',
'sv_mass',
'sv_ntracks',
'sv_chi2',
'sv_normchi2',
'sv_dxy',
'sv_dxysig',
'sv_d3d',
'sv_d3dsig',
'sv_costhetasvpv',
'sv_enratio',
]

n_vtx = 4

reduced_truth = ['isB','isBB','isLeptonicB','isC','isUDS','isG']

DeepFlavour_all_branches = global_branches + cpf_branches + vtx_branches


"""
DeepCSV
"""

DeepCSV_global_branches = [
                            'jet_pt', 'jet_eta',
                            'TagVarCSV_jetNSecondaryVertices',
                            'TagVarCSV_trackSumJetEtRatio',
                            'TagVarCSV_trackSumJetDeltaR',
                            'TagVarCSV_vertexCategory',
                            'TagVarCSV_trackSip2dValAboveCharm',
                            'TagVarCSV_trackSip2dSigAboveCharm',
                            'TagVarCSV_trackSip3dValAboveCharm',
                            'TagVarCSV_trackSip3dSigAboveCharm',
                            'TagVarCSV_jetNSelectedTracks',
                            'TagVarCSV_jetNTracksEtaRel'
                            ]

DeepCSV_track_branches = ['TagVarCSVTrk_trackJetDistVal',
                          'TagVarCSVTrk_trackPtRel',
                          'TagVarCSVTrk_trackDeltaR',
                          'TagVarCSVTrk_trackPtRatio',
                          'TagVarCSVTrk_trackSip3dSig',
                          'TagVarCSVTrk_trackSip2dSig',
                          'TagVarCSVTrk_trackDecayLenVal']

DeepCSV_eta_rel_branches = ['TagVarCSV_trackEtaRel']

DeepCSV_vtx_branches = ['TagVarCSV_vertexMass',
                          'TagVarCSV_vertexNTracks',
                          'TagVarCSV_vertexEnergyRatio',
                          'TagVarCSV_vertexJetDeltaR',
                          'TagVarCSV_flightDistance2dVal',
                          'TagVarCSV_flightDistance2dSig',
                          'TagVarCSV_flightDistance3dVal',
                          'TagVarCSV_flightDistance3dSig']

DeepCSV_all_branches = DeepCSV_global_branches + DeepCSV_track_branches + DeepCSV_eta_rel_branches + DeepCSV_vtx_branches

new_ntuple_keys =  [
                     'Jet_pt',
                     'Jet_eta',
                     'TagVarCSV_jetNSecondaryVertices',
                     'TagVarCSV_trackSumJetEtRatio',
                     'TagVarCSV_trackSumJetDeltaR',
                     'TagVarCSV_vertexCategory',
                     'TagVarCSV_trackSip2dValAboveCharm',
                     'TagVarCSV_trackSip2dSigAboveCharm',
                     'TagVarCSV_trackSip3dValAboveCharm',
                     'TagVarCSV_trackSip3dSigAboveCharm',
                     'TagVarCSV_jetNTracksEtaRel',
                     'TagVarCSV_trackEtaRel',
                     'TagVarCSV_vertexMass',
                     'TagVarCSV_vertexNTracks',
                     'TagVarCSV_vertexEnergyRatio',
                     'TagVarCSV_vertexJetDeltaR',
                     'TagVarCSV_flightDistance2dVal',
                     'TagVarCSV_flightDistance2dSig',
                     'TagVarCSV_flightDistance3dVal',
                     'TagVarCSV_flightDistance3dSig',
                     'TagVarCSV_trackDecayLenVal',
                     'TagVarCSV_trackSip2dSig',
                     'TagVarCSV_trackSip3dSig',
                     'TagVarCSV_trackPtRatio',
                     'TagVarCSV_trackDeltaR',
                     'TagVarCSV_jetNTracks',
                     'TagVarCSV_trackPtRel',
                     'TagVarCSV_trackJetDistVal',
                     'Jet_isUndefined',
                     'Jet_isB',
                     'Jet_isBB',
                     'Jet_isGBB',
                     'Jet_isLeptonicB',
                     'Jet_isLeptonicB_C',
                     'Jet_isC',
                     'Jet_isGCC',
                     'Jet_isCC',
                     'Jet_isUD',
                     'Jet_isG',
                     'Jet_isS',
                     'Jet_DeepFlavourBDisc',
                     'Jet_DeepFlavourCvsLDisc',
                     'Jet_DeepFlavourCvsBDisc',
                     'Jet_DeepFlavourB',
                     'Jet_DeepFlavourBB',
                     'Jet_DeepFlavourLEPB',
                     'Jet_DeepFlavourC',
                     'Jet_DeepFlavourUDS',
                     'Jet_DeepFlavourG',
                     'Jet_DeepCSVBDisc',
                     'Jet_DeepCSVBDiscN',
                     'Jet_DeepCSVCvsLDisc',
                     'Jet_DeepCSVCvsLDiscN',
                     'Jet_DeepCSVCvsBDisc',
                     'Jet_DeepCSVCvsBDiscN',
                     'Jet_DeepCSVb',
                     'Jet_DeepCSVc',
                     'Jet_DeepCSVl',
                     'Jet_DeepCSVbb',
                     'Jet_DeepCSVcc',
                     'Jet_DeepCSVbN',
                     'Jet_DeepCSVcN',
                     'Jet_DeepCSVlN',
                     'Jet_DeepCSVbbN',
                     'Jet_DeepCSVccN',
                     'DeepFlavourInput_charged_btagpf_trackEtaRel',
                     'DeepFlavourInput_charged_btagpf_trackPtRel',
                     'DeepFlavourInput_charged_btagpf_trackPPar',
                     'DeepFlavourInput_charged_btagpf_trackDeltaR',
                     'DeepFlavourInput_charged_btagpf_trackPParRatio',
                     'DeepFlavourInput_charged_btagpf_trackSip2dVal',
                     'DeepFlavourInput_charged_btagpf_trackSip2dSig',
                     'DeepFlavourInput_charged_btagpf_trackSip3dVal',
                     'DeepFlavourInput_charged_btagpf_trackSip3dSig',
                     'DeepFlavourInput_charged_btagpf_trackJetDistVal',
                     'DeepFlavourInput_charged_ptrel',
                     'DeepFlavourInput_charged_drminsv',
                     'DeepFlavourInput_charged_VTX_ass',
                     'DeepFlavourInput_charged_puppiw',
                     'DeepFlavourInput_charged_chi2',
                     'DeepFlavourInput_charged_quality',
                     'DeepFlavourInput_neutral_ptrel',
                     'DeepFlavourInput_neutral_deltaR',
                     'DeepFlavourInput_neutral_isGamma',
                     'DeepFlavourInput_neutral_hadFrac',
                     'DeepFlavourInput_neutral_drminsv',
                     'DeepFlavourInput_neutral_puppiw',
                     'DeepFlavourInput_sv_pt',
                     'DeepFlavourInput_sv_deltaR',
                     'DeepFlavourInput_sv_mass',
                     'DeepFlavourInput_sv_ntracks',
                     'DeepFlavourInput_sv_chi2',
                     'DeepFlavourInput_sv_normchi2',
                     'DeepFlavourInput_sv_dxy',
                     'DeepFlavourInput_sv_dxysig',
                     'DeepFlavourInput_sv_d3d',
                     'DeepFlavourInput_sv_d3dsig',
                     'DeepFlavourInput_sv_costhetasvpv',
                     'DeepFlavourInput_sv_enratio'
                     ]


key_lookup = {'Jet_pt': 'Jet_pt',
	'Jet_eta': 'Jet_eta',
	'TagVarCSV_jetNSecondaryVertices': 'TagVarCSV_jetNSecondaryVertices',
	'TagVarCSV_trackSumJetEtRatio': 'TagVarCSV_trackSumJetEtRatio',
	'TagVarCSV_trackSumJetDeltaR': 'TagVarCSV_trackSumJetDeltaR',
	'TagVarCSV_vertexCategory': 'TagVarCSV_vertexCategory',
	'TagVarCSV_trackSip2dValAboveCharm': 'TagVarCSV_trackSip2dValAboveCharm',
	'TagVarCSV_trackSip2dSigAboveCharm': 'TagVarCSV_trackSip2dSigAboveCharm',
	'TagVarCSV_trackSip3dValAboveCharm': 'TagVarCSV_trackSip3dValAboveCharm',
	'TagVarCSV_trackSip3dSigAboveCharm': 'TagVarCSV_trackSip3dSigAboveCharm',
	'TagVarCSV_jetNTracksEtaRel': 'TagVarCSV_jetNTracksEtaRel',
	'TagVarCSV_trackEtaRel': 'TagVarCSV_trackEtaRel',
	'TagVarCSV_vertexMass': 'TagVarCSV_vertexMass',
	'TagVarCSV_vertexNTracks': 'TagVarCSV_vertexNTracks',
	'TagVarCSV_vertexEnergyRatio': 'TagVarCSV_vertexEnergyRatio',
	'TagVarCSV_vertexJetDeltaR': 'TagVarCSV_vertexJetDeltaR',
	'TagVarCSV_flightDistance2dVal': 'TagVarCSV_flightDistance2dVal',
	'TagVarCSV_flightDistance2dSig': 'TagVarCSV_flightDistance2dSig',
	'TagVarCSV_flightDistance3dVal': 'TagVarCSV_flightDistance3dVal',
	'TagVarCSV_flightDistance3dSig': 'TagVarCSV_flightDistance3dSig',
	'TagVarCSV_trackDecayLenVal': 'TagVarCSV_trackDecayLenVal',
	'TagVarCSV_trackSip2dSig': 'TagVarCSV_trackSip2dSig',
	'TagVarCSV_trackSip3dSig': 'TagVarCSV_trackSip3dSig',
	'TagVarCSV_trackPtRatio': 'TagVarCSV_trackPtRatio',
	'TagVarCSV_trackDeltaR': 'TagVarCSV_trackDeltaR',
	'TagVarCSV_jetNTracks': 'TagVarCSV_jetNTracks',
	'TagVarCSV_trackPtRel': 'TagVarCSV_trackPtRel',
	'TagVarCSV_trackJetDistVal': 'TagVarCSV_trackJetDistVal',
	'Jet_isB': 'Jet_isB',
	'Jet_isBB': 'Jet_isBB',
	'Jet_isGBB': 'Jet_isGBB',
	'Jet_isLeptonicB': 'Jet_isLeptonicB',
	'Jet_isLeptonicB_C': 'Jet_isLeptonicB_C',
	'Jet_isC': 'Jet_isC',
	'Jet_isGCC': 'Jet_isGCC',
	'Jet_isCC': 'Jet_isCC',
	'Jet_isUD': 'Jet_isUD',
	'Jet_isS': 'Jet_isS',
	'Jet_isG': 'Jet_isG',
	'DeepFlavourInput_charged_btagpf_trackEtaRel': 'DeepFlavourInput_charged_btagpf_trackEtaRel',
	'DeepFlavourInput_charged_btagpf_trackPtRel': 'DeepFlavourInput_charged_btagpf_trackPtRel',
	'DeepFlavourInput_charged_btagpf_trackPPar': 'DeepFlavourInput_charged_btagpf_trackPPar',
	'DeepFlavourInput_charged_btagpf_trackDeltaR': 'DeepFlavourInput_charged_btagpf_trackDeltaR',
	'DeepFlavourInput_charged_btagpf_trackPParRatio': 'DeepFlavourInput_charged_btagpf_trackPParRatio',
	'DeepFlavourInput_charged_btagpf_trackSip2dVal': 'DeepFlavourInput_charged_btagpf_trackSip2dVal',
	'DeepFlavourInput_charged_btagpf_trackSip2dSig': 'DeepFlavourInput_charged_btagpf_trackSip2dSig',
	'DeepFlavourInput_charged_btagpf_trackSip3dVal': 'DeepFlavourInput_charged_btagpf_trackSip3dVal',
	'DeepFlavourInput_charged_btagpf_trackSip3dSig': 'DeepFlavourInput_charged_btagpf_trackSip3dSig',
	'DeepFlavourInput_charged_btagpf_trackJetDistVal': 'DeepFlavourInput_charged_btagpf_trackJetDistVal',
	'DeepFlavourInput_charged_ptrel': 'DeepFlavourInput_charged_ptrel',
	'DeepFlavourInput_charged_drminsv': 'DeepFlavourInput_charged_drminsv',
	'DeepFlavourInput_charged_VTX_ass':   'DeepFlavourInput_charged_VTX_ass',
	'DeepFlavourInput_charged_puppiw':   'DeepFlavourInput_charged_puppiw',
	'DeepFlavourInput_charged_chi2':  'DeepFlavourInput_charged_chi2',
	'DeepFlavourInput_charged_quality': 'DeepFlavourInput_charged_quality',
	'DeepFlavourInput_neutral_ptrel': 'DeepFlavourInput_neutral_ptrel',
	'DeepFlavourInput_neutral_deltaR': 'DeepFlavourInput_neutral_deltaR',
	'DeepFlavourInput_neutral_isGamma': 'DeepFlavourInput_neutral_isGamma',
	'DeepFlavourInput_neutral_hadFrac': 'DeepFlavourInput_neutral_hadFrac',
	'DeepFlavourInput_neutral_drminsv': 'DeepFlavourInput_neutral_drminsv',
	'DeepFlavourInput_neutral_puppiw': 'DeepFlavourInput_neutral_puppiw',
	'DeepFlavourInput_sv_pt': 'DeepFlavourInput_sv_pt',
	'DeepFlavourInput_sv_deltaR': 'DeepFlavourInput_sv_deltaR',
	'DeepFlavourInput_sv_mass': 'DeepFlavourInput_sv_mass',
	'DeepFlavourInput_sv_ntracks': 'DeepFlavourInput_sv_ntracks',
	'DeepFlavourInput_sv_chi2': 'DeepFlavourInput_sv_chi2',
	'DeepFlavourInput_sv_normchi2': 'DeepFlavourInput_sv_normchi2',
	'DeepFlavourInput_sv_dxy': 'DeepFlavourInput_sv_dxy',
	'DeepFlavourInput_sv_dxysig': 'DeepFlavourInput_sv_dxysig',
	'DeepFlavourInput_sv_d3d': 'DeepFlavourInput_sv_d3d',
	'DeepFlavourInput_sv_d3dsig': 'DeepFlavourInput_sv_d3dsig',
	'DeepFlavourInput_sv_costhetasvpv': 'DeepFlavourInput_sv_costhetasvpv',
	'DeepFlavourInput_sv_enratio': 'DeepFlavourInput_sv_enratio'
        }


file_comparison = [ {"QCD_PT_470to600": ( ["/eos/home-s/sewuchte/BTV-Phase2/December_TDR/hadded/HLT_TRKv06p1_TICL/Phase2HLTTDR_QCD_Pt470to600_14TeV_PU140_HLT_TRKv06p1_TICL_cutsV2.root", "/eos/home-s/sewuchte/BTV-Phase2/December_TDR/hadded/HLT_TRKv06p1_TICL/Phase2HLTTDR_QCD_Pt470to600_14TeV_PU200_HLT_TRKv06p1_TICL_cutsV2.root"], ["/eos/cms/store/group/phys_btag/HLTRetraining/offline_training_files/QCD_Pt_470to600_TuneCP5_14TeV_pythia8.root"])
    },
    {"TT_TuneCP5_14TeV-powheg-pythia8": ( ["eos/home-s/sewuchte/BTV-Phase2/December_TDR/hadded/HLT_TRKv00_TICL/Phase2HLTTDR_TTbar_14TeV_PU200_HLT_TRKv00_TICL_default.root"], ["/eos/cms/store/group/phys_btag/HLTRetraining/offline_training_files/TT_TuneCP5_14TeV-powheg-pythia8.root"])}
    ]
