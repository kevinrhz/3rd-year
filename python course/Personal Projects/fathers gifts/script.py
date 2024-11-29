import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

# Gift class with added `image_path` attribute for images
class Gift:
    def __init__(self, year, price, name, description, image_path):
        self.year = year
        self.name = name
        self.price = price
        self.description = description
        self.image_path = image_path

    def get_summary(self):
        return f"In {self.year}, Dad gave me a {self.name}: {self.description} (Cost: {self.price})"

# All your original gifts with placeholder image paths
gifts = [
    Gift(2007, "$300", "Wii", "A brand-new Wii console that introduced me to a world of interactive gaming.", "path/to/wii_image.png"),
    Gift(2008, "$200", "Nintendo DS", "A handheld Nintendo DS, allowing me to take my favorite games anywhere.", "path/to/nintendo_ds_image.png"),
    Gift(2010, "$300", "Nintendo 3DS", "An upgraded Nintendo 3DS, bringing a 3D experience to gaming.", "path/to/nintendo_3ds_image.png"),
    Gift(2013, "$300", "Xbox 360", "A powerful Xbox 360 console that introduced me to new genres and online gaming.", "path/to/xbox_image.png"),
    Gift(2014, "$500", "Cannondale Bike", "A sturdy Cannondale bike perfect for both casual rides and adventurous trails.", "path/to/cannondale_bike_image.png"),
    Gift(2015, "$1500", "Camera", "A high-quality camera that kickstarted my passion for photography.", "path/to/camera_image.png"),
    Gift(2016, "$5000", "Whistler Trip", "An exhilarating trip to Whistler, filled with outdoor adventures and scenic views.", "path/to/whistler_trip_image.png"),
    Gift(2017, "$2000", "Kona Bike", "An impressive Kona bike designed for serious riders.", "path/to/kona_bike_image.png"),
    Gift(2018, "$10000", "Europe Trip", "A life-changing trip to Europe, exploring iconic cities and historic landmarks.", "path/to/europe_trip_image.png"),
    Gift(2019, "$30000", "BMW", "A stunning BMW model car, a symbol of my dream to own one someday.", "cslHommage.jpg"),
    Gift(2020, "$1500", "Home Gym", "A home gym setup to support my fitness goals.", "path/to/home_gym_image.png"),
    Gift(2021, "$6000", "Trek Bike", "A high-performance Trek bike designed for cycling enthusiasts.", "path/to/trek_bike_image.png"),
    Gift(2022, "$2500", "MacBook Pro", "A powerful MacBook Pro that transformed my work and creativity.", "path/to/macbook_image.png"),
    Gift(2023, "$2500", "Spain Trip", "An adventurous trip to Spain, with its rich culture, vibrant cities, and amazing food.", "path/to/spain_trip_image.png")
]

# Organize gifts by year for easier access in the app
gifts_by_year = {}
for gift in gifts:
    if gift.year not in gifts_by_year:
        gifts_by_year[gift.year] = []
    gifts_by_year[gift.year].append(gift)

# Main application window
class GiftApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Father's Gifts")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Top Layout for Year Selector
        top_layout = QHBoxLayout()

        # Year dropdown menu
        self.year_dropdown = QComboBox()
        self.year_dropdown.addItems([str(year) for year in sorted(gifts_by_year.keys())])
        self.year_dropdown.currentIndexChanged.connect(self.change_year)
        top_layout.addWidget(self.year_dropdown, alignment=Qt.AlignTop | Qt.AlignLeft)

        # Image display (central part of UI)
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setPixmap(QPixmap("path/to/default_image.png").scaled(self.width(), self.height(), Qt.KeepAspectRatio))

        # Add components to main layout
        self.layout.addLayout(top_layout)
        self.layout.addWidget(self.image_label)

        # Navigation buttons
        left_button = QPushButton("<")
        right_button = QPushButton(">")

        left_button.setFixedSize(50, 50)
        right_button.setFixedSize(50, 50)

        left_button.clicked.connect(self.previous_gift)
        right_button.clicked.connect(self.next_gift)

        # Overlay buttons on the left and right
        self.layout.addWidget(left_button, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        self.layout.addWidget(right_button, alignment=Qt.AlignRight | Qt.AlignVCenter)

        # Initialize gift data
        self.current_year = int(self.year_dropdown.currentText())
        self.current_gift_index = 0
        self.update_image()

    def change_year(self):
        self.current_year = int(self.year_dropdown.currentText())
        self.current_gift_index = 0
        self.update_image()

    def previous_gift(self):
        if self.current_gift_index > 0:
            self.current_gift_index -= 1
        else:
            self.current_gift_index = len(gifts_by_year[self.current_year]) - 1
        self.update_image()

    def next_gift(self):
        if self.current_gift_index < len(gifts_by_year[self.current_year]) - 1:
            self.current_gift_index += 1
        else:
            self.current_gift_index = 0
        self.update_image()

    def update_image(self):
        # Get the current gift
        gift_list = gifts_by_year.get(self.current_year, [])
        if gift_list:
            current_gift = gift_list[self.current_gift_index]
            # Load and display the image
            pixmap = QPixmap(current_gift.image_path).scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)
        else:
            # Default text if no gifts are available for the year
            self.image_label.setText("No gifts available for this year")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GiftApp()
    window.show()
    sys.exit(app.exec_())
