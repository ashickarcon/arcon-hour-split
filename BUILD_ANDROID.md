# Arcon Hour Split - Android Build Guide

## 📱 Build Android APK

### Option A: Using GitHub Actions (Easiest - No Linux needed!)

1. **Create a GitHub repository** and push these files:
   - `hour_split_kivy.py` (rename to `main.py`)
   - `buildozer.spec`
   - `requirements.txt`

2. **Create `.github/workflows/build.yml`** with:
```yaml
name: Build Android APK
on: [push, workflow_dispatch]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build with Buildozer
        uses: ArtemSBulgakov/buildozer-action@v1
        id: buildozer
        with:
          workdir: .
          buildozer_version: stable
      - name: Upload APK
        uses: actions/upload-artifact@v2
        with:
          name: package
          path: ${{ steps.buildozer.outputs.filename }}
```

3. **Push to GitHub** → Actions tab → Download APK when done!

---

### Option B: Using WSL/Linux (Local Build)

1. **Install WSL** (if on Windows):
```bash
wsl --install Ubuntu
```

2. **Inside WSL, install dependencies**:
```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip3 install --user buildozer cython==0.29.33
```

3. **Rename the Kivy file**:
```bash
mv hour_split_kivy.py main.py
```

4. **Build APK**:
```bash
buildozer android debug
```

5. **Find APK** in `bin/` folder:
```bash
ls bin/*.apk
```

---

### Option C: Using Google Colab (Cloud Build)

1. Go to [Google Colab](https://colab.research.google.com)
2. Run this notebook:

```python
!pip install buildozer cython==0.29.33
!sudo apt install -y openjdk-17-jdk

# Upload your files or clone from GitHub
from google.colab import files
# Upload main.py, buildozer.spec, requirements.txt

!buildozer android debug

# Download the APK
from google.colab import files
files.download('bin/arconsplit-1.0-arm64-v8a-debug.apk')
```

---

## 📥 Install on Android

1. **Transfer APK** to your phone (via USB, email, or cloud)
2. **Enable "Install from Unknown Sources"** in Settings
3. **Tap the APK** to install
4. **Open "Arcon Hour Split"** app!

---

## 🧪 Test Locally First (Windows)

Before building for Android, test the Kivy app on your PC:

```powershell
pip install kivy
python hour_split_kivy.py
```

---

## 📝 Important Notes

- **Rename `hour_split_kivy.py` to `main.py`** before building
- First build takes 20-30 minutes (downloads Android SDK/NDK)
- Subsequent builds are faster (~5 minutes)
- **GitHub Actions is recommended** - easiest and no local setup needed!
