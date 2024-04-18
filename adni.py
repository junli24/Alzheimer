import nibabel as nib
import matplotlib.pyplot as plt

# Path to your NIfTI file
nii_file_path = 'D:\processed_data\mri\wmI37577.nii'

# Load the NIfTI file
nii = nib.load(nii_file_path)

# Get the NIfTI data array
nii_data = nii.get_fdata()

print(type(nii_data))

# Display the NIfTI image
# plt.figure(figsize=(8, 8))
# plt.imshow(nii_data[:, :, 50], cmap='gray')  # Display a middle slice
# plt.axis('off')
# plt.show()
