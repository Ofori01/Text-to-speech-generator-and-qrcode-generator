import io
import qrcode
import PySimpleGUI as sg

sg.theme('Material1')
class QRCodeGenerator:
    def __init__(self):
        self.layout = [
            [sg.Text('Enter text to generate QR code:'), sg.Input(key='-DATA-')],
            [sg.Text("Select fill color:"), sg.Combo(['black', 'white', 'red', 'green', 'blue'], key='-FILL_COLOR-', default_value= 'black')],
            [sg.Text("Select background color:"), sg.Combo(['white', 'black', 'red', 'green', 'blue'], key='-BACK_COLOR-', default_value= 'white')],
            [sg.Text("Select box size:"), sg.Combo([5, 6, 7, 8, 9], key='-BOX_SIZE-', default_value= '4')],
            [sg.Text("Select border size:"), sg.Combo([1, 2, 3, 4, 5], key='-BORDER_SIZE-', default_value='4')],
            [sg.Button("Generate QR Code"), sg.Button("Exit")],
            [sg.Image(key='-IMAGE-')]
        ]

        self.window = sg.Window("QR Code Generator", self.layout)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == "Exit":
                break
            elif event == "Generate QR Code":
                data = values['-DATA-']
                fill_color = values['-FILL_COLOR-']
                back_color = values['-BACK_COLOR-']
                box_size = values['-BOX_SIZE-']
                border_size = values['-BORDER_SIZE-']
            if not data:
                    sg.popup('Please enter some text.')
                    continue
                # Generate the QR code
            try:
                    

                qr = qrcode.QRCode(version=1, box_size=int(box_size), border=int(border_size))
                qr.add_data(data)
                qr.make(fit=True)
                img = qr.make_image(fill_color=fill_color, back_color=back_color)

                    # Make the image look nicer
                img = img.resize((300, 300))
                img = img.convert('RGB')

                    # Display the QR code
                bio = io.BytesIO()
                img.save(bio, format='PNG')
                self.window['-IMAGE-'].update(data=bio.getvalue())
            except Exception as e:
                sg.popup("Error", f"QR code generation failed: {e}")
                self['-QR-'].update(data=b'')

        self.window.close()


if __name__ == '__main__':
    qr_gen = QRCodeGenerator()
    qr_gen.run()
