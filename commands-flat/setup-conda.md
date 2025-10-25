Set up and optimize conda environments tailored to system hardware.

Your task:
1. Evaluate current conda setup:
   ```bash
   conda env list  # List environments
   conda list -n env_name  # Packages in environment
   ```

2. Validate hardware specifications:
   - Check for NVIDIA GPU (nvidia-smi)
   - CPU information (lscpu)
   - Available RAM
   - Storage capacity

3. Create optimized environment based on hardware:
   - For systems with NVIDIA GPU:
     - Include CUDA toolkit
     - GPU-accelerated libraries (cuDNN, cuBLAS)
     - PyTorch/TensorFlow with GPU support

   - For CPU-only systems:
     - CPU-optimized libraries
     - Intel MKL if on Intel CPU
     - Standard ML libraries

4. Best practices:
   - Use mamba for faster package resolution
   - Create environment from environment.yml
   - Pin versions for reproducibility
   - Separate environments for different projects

5. Example environment setup:
   ```bash
   # Create environment
   conda create -n myenv python=3.11

   # Activate and install packages
   conda activate myenv
   conda install numpy pandas scikit-learn

   # For GPU systems
   conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
   ```

Ensure conda environments are optimized for the user's specific hardware configuration.
