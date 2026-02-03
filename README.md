# MarshalleDD

**Professional Drawing Management & Reporting Solution for Engineering**

[![Version](https://img.shields.io/badge/version-1.0-blue.svg)](https://github.com/EddPalenciaV/DeveD_Marshal)
[![License](https://img.shields.io/badge/license-Proprietary-red.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)](https://www.python.org/)

---

## Overview

**MarshalleDD** is a professional drawing management system designed specifically for engineering and architectural firms. It automates the process of cleaning, sorting, tagging, and generating comprehensive reports for technical drawings. The application is built with a modern graphical user interface and provides robust functionality for handling large drawing databases.

### Key Capabilities

- **Drawing Cleanup**: Automatically removes revision tags and optimizes filenames
- **Revision Management**: Tags drawings with revision information
- **Transmittal Generation**: Creates professional PDF transmittals from Excel data
- **Department Filtering**: Separates drawings by discipline for better workflow management
- **PDF Report Generation**: Generates comprehensive drawing reports in PDF format

---

## Features

✨ **Modern GUI Interface**

- Built with PySide6 for a responsive, professional user experience
- Real-time output logging and execution feedback
- Splash screen with version information

📁 **Drawing Management**

- Batch processing of PDF files
- Automatic name revision tag removal and insertion
- Department-based organization (e.g. Civil, Structural, Architectural)
- Pattern-based drawing filtering

📊 **Report Generation**

- Automatic PDF transmittal creation from Excel transmittal files
- Multi-sheet Excel support (e.g. CIVIL, STRUCTURE, ARCHITECT)
- Professional formatting with A4 paper size

🔐 **Security & Licensing**

- PyArmor encryption support
- Expiration date and license key integration
- Single-file executable distribution

---

## System Requirements

### Minimum Requirements

- **OS**: Windows 7 or later (64-bit)
- **Python**: 3.9 or higher
- **Memory**: 4GB RAM
- **Disk Space**: 500MB

### For Development

- **Python**: 3.9+
- **Virtual Environment**: venv (recommended)
- **Git**: For version control

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/EddPalenciaV/DeveD_Marshal.git
cd DeveD_Marshal
```

### 2. Create Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Application

```powershell
python DeveD_Marshal.py
```

---

## Dependencies

### Core Libraries

- **PySide6** (6.x) - GUI framework
- **openpyxl** - Excel file handling and reading
- **xlwings** - Excel automation and integration
- **win32com-client** (pywin32) - Windows COM interface for MS Office

### PDF & Image Processing

- **PyMuPDF** (fitz) - PDF manipulation and analysis
- **Pillow** (PIL) - Image processing

For a complete list, see [requirements.txt](requirements.txt)

---

## Project Structure

```
DeveD_Marshal/
├── DeveD_Marshal.py          # Main application entry point & UI
├── Revisionator.py           # Drawing revision tag management
├── pdf_Organiser.py          # PDF organization & department sorting
├── Transmit_Auto1000.py      # Transmittal PDF generation
├── requirements.txt          # Python dependencies
├── MarshaleDD_small001.png   # Application logo/splash screen
└── README.md                 # This file
```

### Module Descriptions

| Module                 | Purpose                                                      |
| ---------------------- | ------------------------------------------------------------ |
| `DeveD_Marshal.py`     | Main GUI application with button handlers and output dialogs |
| `Revisionator.py`      | Removes revision tags from filenames and applies new tags    |
| `pdf_Organiser.py`     | Organizes PDFs by department and manages superseding         |
| `Transmit_Auto1000.py` | Generates transmittal PDFs from Excel source files           |

---

## Usage

### Starting the Application

```powershell
.\venv\Scripts\Activate.ps1
python DeveD_Marshal.py
```

### Main Functions

#### 1. **MarshalleDD** (Complete Workflow)

Executes the full drawing management pipeline:

- Supersedes existing drawings across departments
- Removes revision tags
- Applies new revision information
- Generates transmittal PDF

#### 2. **Supersede Drawings**

Organizes and supersedes drawings by department:

- **Option 1**: All drawings together in \_SS folder
- **Option 2**: Separated by department (CIVIL, ARCHITECTURAL, STRUCTURAL)

#### 3. **Fix Revision Tags**

Manages drawing revision information:

- Removes existing revision tags
- Applies new tags with current revision data

#### 4. **Generate Transmittal PDF**

Creates professional transmittal documents:

- Reads data from Excel transmittal files
- Generates formatted PDF output
- Supports multiple departments

---

## Configuration

### File Paths

- Place PDF drawings in the current working directory
- Ensure Excel transmittal files in use or Template are in the working directory
- Application creates `_SS` subdirectory for organized drawings

### Excel Transmittal Format

Transmittal files must contain the following sheets:

- `CIVIL` - Civil engineering drawings
- `STRUCTURE` - Structural drawings
- `ARCHITECT` - Architectural drawings

---

## Troubleshooting

### Common Issues

**"No module named 'PySide6'"**

```powershell
pip install PySide6 --upgrade
```

**"Cannot find Excel file"**

- Ensure transmittal file is in the current directory
- Check file naming follows: `Transmittal YYMMDD.xlsx`

**Drawing files not found**

- Verify PDF files are in the working directory
- Check filenames contain department code (e.g., `-C-`, `-A-`, `-S-`)

---

## Version History

| Version | Date       | Changes                              |
| ------- | ---------- | ------------------------------------ |
| 1.0     | 22/01/2026 | Initial release - Core functionality |

---

## About

**MarshalleDD** is developed and maintained by **Edd Palencia-Vanegas** as part of **DeveD Software Pty Ltd**

### Company Information

- **Company**: DeveD Software Pty Ltd
- **Owner and Developer**: Edd Palencia-Vanegas
- **Industry Focus**: Engineering & Architecture
- **Contact**: eddpalencia24@gmail.com

---

## License

This software is proprietary and confidential. Unauthorized copying or distribution is prohibited.

For licensing inquiries, please contact Edd Palencia-Vanegas by email: eddpalencia24@gmail.com.

---

## Support

For bug reports, feature requests, or technical support, please contact:

- **Email**: eddpalencia24@gmail.com
- **GitHub Issues**: [\[GitHub Issues Link\]](https://github.com/EddPalenciaV/DeveD_Marshal/issues)

---

## Contributing

This is a proprietary project. For contribution opportunities, please contact the developer.

---

## Disclaimer

This software is a product meant to be a showcase for clients, not for distribution.
The final distribution version of this software needs to be adapted to individual business's systems.
This software product can only be distributed by Deved Software Pty Ltd and/or Edd Palencia-Vanegas.

---

**© 2026 DeveD Software Pty Ltd. All rights reserved.**
