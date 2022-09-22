name: AWS
on: workflow_dispatch

jobs:
  build:

    runs-on: windows-latest
    timeout-minutes: 9999

    steps:

    - name: Download ngrok
      run: |
        Invoke-WebRequest https://raw.githubusercontent.com/sadiknabil/ngrok-rdp/main/resources/ngrok.zip -OutFile ngrok.zip
        Invoke-WebRequest https://raw.githubusercontent.com/sadiknabil/ngrok-rdp/main/resources/start.bat -OutFile start.bat
        Invoke-WebRequest https://raw.githubusercontent.com/sadiknabil/ngrok-rdp/main/resources/winrar.exe -OutFile winrar.exe
    - name: Extract ngrok Files
      run: Expand-Archive ngrok.zip

    - name: Connecting ngrok Account
      run: .\ngrok\ngrok.exe authtoken $Env:NGROK_AUTH_TOKEN
      env:
        NGROK_AUTH_TOKEN: ${{ secrets.NGROK_AUTH_TOKEN }}

    - name: Enable RDP Access
      run: |
        Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server'-name "fDenyTSConnections" -Value 0
        Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
        Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name "UserAuthentication" -Value 1
        copy winrar.exe C:\Users\Public\Desktop\winrar.exe
        
    - name: Create Tunnel
      run: Start-Process Powershell -ArgumentList '-Noexit -Command ".\ngrok\ngrok.exe tcp 3389"'

    - name: Connect to RDP  [CPU 2 Core - 7GB Ram - 256 SSD]
      run: cmd /c start.bat

    - name: Install Winrar
      run: cmd /c C:\Users\Public\Desktop\winrar.exe winrar.exe /s
      
    - name: Clone spotify_bots_account Repository
      run: cmd /c git clone https://github.com/sadiknabil/spotify_bots_account.git C:\Users\Public\Desktop\spotify_bots_account
      
    - name: Start install Spotify Account WS
      run: cmd /c pip install requests
      
    - name: Start Creating Spotify Account
      run: cmd /c python C:\Users\Public\Desktop\spotify_bots_account\main_default_val.py
      
    - name: Clone spotify_bots_streaming Repository
      run: cmd /c git clone https://github.com/sadiknabil/spotify_bots_streaming.git C:\Users\Public\Desktop\spotify_bots_streaming
    
    - name: TimeCount
      run: |
        Invoke-WebRequest https://raw.githubusercontent.com/sadiknabil/ngrok-rdp/main/resources/loop.ps1 -OutFile loop.ps1
        ./loop.ps1
