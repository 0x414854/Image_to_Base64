import base64
import pyperclip
import os

def main():
    file_path = "/Path/to/Your/Image_file.png"
    png_file = os.path.basename(file_path)
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    if file_path.endswith('.png'):
        data_uri = 'data:image/png;base64,' + encoded_string

    elif file_path.endswith('.jpg'):
        data_uri = 'data:image/jpg;base64,' + encoded_string

    else:
        print("Error : File format not supported.")
        return


    print('Data URI :\n', data_uri)
    pyperclip.copy(data_uri)
    print('The URI data chain was copied to the clipboard.')
    save_to_file(data_uri, png_file)

def save_to_file(data_uri, png_file):
    file_name = 'Base64|' + png_file
    if not file_name.endswith('.txt'):
        file_name = file_name + '.txt'
    directory = "/Output/Path/"
    file_path = os.path.join(directory, file_name)
    with open(file_path, "w") as file:
        file.write(data_uri)
    print("Data URI saved at : ", file_path)

main()