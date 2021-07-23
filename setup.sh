# get basedirectory
export BTVHLTToolsDirectory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# source DeepJet env

export TrainingVersion="test_01"
export OnlineDirectory=/nfs/dust/cms/user/neich/BTV/Trainings
export OnlineTrainingFiles=/nfs/dust/cms/user/neich/BTV/Trainings/djdc_files/${TrainingVersion}/dataCollection.djcdc
export OnlineEvaluationFiles=${OnlineDirectory}/evaluation_filelist.txt
source $BTVHLTToolsDirectory/DeepJet/env.sh

export PYTHONPATH=$BTVHLTToolsDirectory:$PYTHONPATH
export PYTHONPATH=$BTVHLTToolsDirectory/DeepJetCore:$PYTHONPATH
export PYTHONPATH=$BTVHLTToolsDirectory/DeepJetCore/compiled:$PYTHONPATH
export PYTHONPATH=$BTVHLTToolsDirectory/DeepJetCore/conversion:$PYTHONPATH
export PYTHONPATH=$BTVHLTToolsDirectory/DeepJet/modules:$PYTHONPATH
export PYTHONPATH=$BTVHLTToolsDirectory/DeepJet/modules/models:$PYTHONPATH

export LD_LIBRARY_PATH=$BTVHLTToolsDirectory/DeepJetCore/compiled:$LD_LIBRARY_PATH

if test -f "$BTVHLTToolsDirectory/local_setup.sh";
then
    source local_setup.sh
else
    echo "No local_setup.sh found! Using defaults for env vars"
fi

export TrainingOutput=/nfs/dust/cms/user/neich/BTV/Trainings

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

