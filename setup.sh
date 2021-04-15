# get basedirectory
export BTVHLTToolsDirectory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# source DeepJet env
export TrainingVersion="out_01"
export BTVHLTTrainingFile=/eos/cms/store/group/phys_btag/HLTRetraining/PhaseII/Online/HLTTDR_February2021/HLT_TRKv00_default/jet_shaped
export OfflineDirectory=/eos/cms/store/group/phys_btag/HLTRetraining/PhaseII/Offline/Max_deepntuplizer_11_2_pv3d_newTrackCollection/pu140/
export OfflineTrainingFiles=${OfflineDirectory}/djdc_files/${TrainingVersion}/dataCollection.djdc
source $BTVHLTToolsDirectory/DeepJet/env.sh

if test -f "$BTVHLTToolsDirectory/local_setup.sh";
then
    source local_setup.sh
else
    echo "No local_setup.sh found! Using defaults for env vars"
fi


if [ -z "$TrainingOutput" ]
then
      echo "\$TrainingOutput is empty"
      export TrainingOutput="${BTVHLTToolsDirectory}/training_output"
      if [[ -d $TrainingOutput ]];then
          echo "$TrainingOutput already exists!"
      else
          echo "Creating training-output directory!"
          mkdir $TrainingOutput
      fi
      echo "\$TrainingOutput set to ${TrainingOutput}"
fi
