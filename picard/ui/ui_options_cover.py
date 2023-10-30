# Form implementation generated from reading ui file 'ui/options_cover.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CoverOptionsPage(object):
    def setupUi(self, CoverOptionsPage):
        CoverOptionsPage.setObjectName("CoverOptionsPage")
        CoverOptionsPage.resize(632, 560)
        self.verticalLayout = QtWidgets.QVBoxLayout(CoverOptionsPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.save_images_to_tags = QtWidgets.QGroupBox(CoverOptionsPage)
        self.save_images_to_tags.setCheckable(True)
        self.save_images_to_tags.setChecked(False)
        self.save_images_to_tags.setObjectName("save_images_to_tags")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.save_images_to_tags)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setSpacing(2)
        self.vboxlayout.setObjectName("vboxlayout")
        self.cb_embed_front_only = QtWidgets.QCheckBox(self.save_images_to_tags)
        self.cb_embed_front_only.setObjectName("cb_embed_front_only")
        self.vboxlayout.addWidget(self.cb_embed_front_only)
        self.verticalLayout.addWidget(self.save_images_to_tags)
        self.save_images_to_files = QtWidgets.QGroupBox(CoverOptionsPage)
        self.save_images_to_files.setCheckable(True)
        self.save_images_to_files.setChecked(False)
        self.save_images_to_files.setObjectName("save_images_to_files")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.save_images_to_files)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_use_filename = QtWidgets.QLabel(self.save_images_to_files)
        self.label_use_filename.setObjectName("label_use_filename")
        self.verticalLayout_2.addWidget(self.label_use_filename)
        self.cover_image_filename = QtWidgets.QLineEdit(self.save_images_to_files)
        self.cover_image_filename.setObjectName("cover_image_filename")
        self.verticalLayout_2.addWidget(self.cover_image_filename)
        self.save_images_overwrite = QtWidgets.QCheckBox(self.save_images_to_files)
        self.save_images_overwrite.setObjectName("save_images_overwrite")
        self.verticalLayout_2.addWidget(self.save_images_overwrite)
        self.save_only_one_front_image = QtWidgets.QCheckBox(self.save_images_to_files)
        self.save_only_one_front_image.setObjectName("save_only_one_front_image")
        self.verticalLayout_2.addWidget(self.save_only_one_front_image)
        self.image_type_as_filename = QtWidgets.QCheckBox(self.save_images_to_files)
        self.image_type_as_filename.setObjectName("image_type_as_filename")
        self.verticalLayout_2.addWidget(self.image_type_as_filename)
        self.verticalLayout.addWidget(self.save_images_to_files)
        self.ca_providers_groupbox = QtWidgets.QGroupBox(CoverOptionsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ca_providers_groupbox.sizePolicy().hasHeightForWidth())
        self.ca_providers_groupbox.setSizePolicy(sizePolicy)
        self.ca_providers_groupbox.setObjectName("ca_providers_groupbox")
        self.ca_providers_layout = QtWidgets.QVBoxLayout(self.ca_providers_groupbox)
        self.ca_providers_layout.setObjectName("ca_providers_layout")
        self.ca_providers_list = QtWidgets.QListWidget(self.ca_providers_groupbox)
        self.ca_providers_list.setObjectName("ca_providers_list")
        self.ca_providers_layout.addWidget(self.ca_providers_list)
        self.ca_layout = QtWidgets.QHBoxLayout()
        self.ca_layout.setObjectName("ca_layout")
        self.move_label = QtWidgets.QLabel(self.ca_providers_groupbox)
        self.move_label.setObjectName("move_label")
        self.ca_layout.addWidget(self.move_label)
        self.up_button = QtWidgets.QToolButton(self.ca_providers_groupbox)
        self.up_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.up_button.setText("")
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-up.png")
        self.up_button.setIcon(icon)
        self.up_button.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.up_button.setAutoRaise(False)
        self.up_button.setObjectName("up_button")
        self.ca_layout.addWidget(self.up_button)
        self.down_button = QtWidgets.QToolButton(self.ca_providers_groupbox)
        self.down_button.setText("")
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-down.png")
        self.down_button.setIcon(icon)
        self.down_button.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.down_button.setObjectName("down_button")
        self.ca_layout.addWidget(self.down_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.ca_layout.addItem(spacerItem)
        self.ca_providers_layout.addLayout(self.ca_layout)
        self.verticalLayout.addWidget(self.ca_providers_groupbox, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(CoverOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(CoverOptionsPage)

    def retranslateUi(self, CoverOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        self.save_images_to_tags.setTitle(_("Embed cover images into tags"))
        self.cb_embed_front_only.setText(_("Embed only a single front image"))
        self.save_images_to_files.setTitle(_("Save cover images as separate files"))
        self.label_use_filename.setText(_("Use the following file name for images:"))
        self.save_images_overwrite.setText(_("Overwrite the file if it already exists"))
        self.save_only_one_front_image.setText(_("Save only a single front image as separate file"))
        self.image_type_as_filename.setText(_("Always use the primary image type as the file name for non-front images"))
        self.ca_providers_groupbox.setTitle(_("Cover Art Providers"))
        self.move_label.setText(_("Reorder Priority:"))
        self.up_button.setToolTip(_("Move selected item up"))
        self.down_button.setToolTip(_("Move selected item down"))
