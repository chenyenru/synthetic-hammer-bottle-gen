# Generate synthetic data
blender YOLO_data_generator.blend --background --python main_script.py

# Draw bounding box
read -p "Do you want to preview pictures by creating a video? (yes/no) " yn

case $yn in 
	[yY] ) echo "Creating Video for previewing";
        break;;
	[nN] ) echo "exiting...";
		exit;;
	* ) echo "invalid response";
		exit 1;;
esac

python3 draw_bounding.py
