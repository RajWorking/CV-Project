#!/bin/bash
#SBATCH -n 1
#SBATCH --gres=gpu:1
#SBATCH -n 10
#SBATCH --mem-per-cpu=2048
#SBATCH --mail-type=ALL
#SBATCH --mail-user=pratyush.priyadarshi@students.iit.ac.in,triansh.sharma@students.iiit.ac.in
#SBATCH -o logs.txt 
#SBATCH --job-name=cv_project
#SBATCH --time=4-00:00:00
#SBATCH --nodelist gnode74

export TF_XLA_FLAGS=--tf_xla_enable_xla_devices
module load cuda/10.2 cudnn/7.6.5-cuda-10.2
python train.py
