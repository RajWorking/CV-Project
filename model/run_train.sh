#!/bin/bash
#SBATCH --gres=gpu:4
#SBATCH -n 40
#SBATCH --mem-per-cpu=2048
#SBATCH --mail-type=ALL
#SBATCH --mail-user=pratyush.priyadarshi@students.iiit.ac.in,triansh.sharma@students.iiit.ac.in
#SBATCH -o logs.txt 
#SBATCH --job-name=cv_project
#SBATCH --time=4-00:00:00
#SBATCH --nodelist gnode74

# export TF_XLA_FLAGS=--tf_xla_enable_xla_devices
module load cuda/11.0 cudnn/8-cuda-11.0
python train2.py
