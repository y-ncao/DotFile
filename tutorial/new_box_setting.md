E5540 laptop config per BIOS:
      * Service Tag         : HP4ZXZ1
      * Asset Tag           : D0020823
      * Mfr Date            : 04/09/2014
      * Ownership Date      : 04/17/2014
      * Express Service Code: 28525349565

      * Memory Installed    : 16384 MB
      * Memory Speed        : 1600 Mhz
      * Memory Tech         : DDR3L SDRAM
      * DIMM A Size         : 8192 MB
      * DIMM B Size         : 8192 MB

      * Processor Type      : Intel Core i7-4600 CPU@2.10 Ghz
      * Core Count          : 2
      * Clock Speed         : 2.10 Ghz
      * L2 Cache            : 512 KB
      * L3 Cache            : 4096 KB

      * 256 GB HDD          : S14VNSAD928110 (SSD)
      * ODD Device          : DVD+/-RW
      * MAC Address         : EC-F4-BB-24-F7-3F

      * Video Controller    : Intel HD Graphics
      * Video BIOS Version  : 2178v15
      * Video Memory        : 64 MB
      * Panel Type          : 15.6 inch FHD
      * Native Resolution   : 1920x1080

      * Audio Controller    : RealTek ALC3226

      * Wi-Fi Device        : Intel Wireless
      * Bluetooh Device     : Installed

      Has a Camera.

Data gleaned from Linux' "dmesg" command:
     * Intel ro/1000 Network Card
     * Samsung SSD
     * Matshita DVD+-RW UJ8FB
     * Intel Dual band Wireless AC 7260
     * UVC 1.00 Laptop Integrated Webcam HD

Data from "lspci" command:
  * VGA: Intel Corporation Haswell - ULT Integrated Graphics Controller (rev 0b)
  * NVIDA Corporation GF117M [Geforce 610M/710M / GT 620M/625M/630M/720M] (rev a1)

After google research, this laptop is using a "Hybrid" video setup. The hardware
uses the Haswell Chipset (Intel Video on board the CPU) until the need for more
video processing power occurs, at which point the hardware switches to the
Nvidia chipset. Linux support for this is very poor (bumblebee and nvidia-prime
projects). It's just not usable at this point. They both require you to run
programs with a wrapper script if you want the nvidia chipset to work.

1. Base Linux Mint installation with:
  * Partitions:
    48 GB (49152 MB) for "/"
    8  GB ( 8192 MB) for "swap"
    Remainder of disk for "/home"

2. Optimize Laptop for SSD usage
   Add the following lines to /etc/rc.local:

       echo deadline >/sys/block/sda/queue/scheduler
       echo 0 > /proc/sys/vm/swappiness

   In /etc/fstab, add the following:

      tmpfs   /tmp       tmpfs   defaults,noatime,mode=1777   0  0
      tmpfs   /var/spool tmpfs   defaults,noatime,mode=1777   0  0
      tmpfs   /var/tmp   tmpfs   defaults,noatime,mode=1777   0  0

3. Was having issues with package downloads.
   * Used the "Software Sources" app to change the "Base" Mirror from a UK to a US mirror
   * Edited the file /etc/gai.conf and change this line:
            #precedence ::ffff:0:0/96   10
     To:
            precedence ::ffff:0:0/96   100
     (uncommented & changed 10->100)

    This forces sites to use IPv4 over IPv6: http://www.buntschu.ch/blog/?p=493
    Was getting HORRIBLE slow down waiting on IPv6 repos

4. Update packages on the box:
   sudo apt-get update
   sudo apt-get upgrade

5. Add extra packages:
   sudo apt-get install keychain chromium-browser firefox pidgin thunderbird python2.7 python2.7-dev python-software-properties python-setuptools python-simplejson python-netaddr python-reportlab python-reportlab-accel python-reportlab-doc python-lxml python-crypto python-pycurl python-ldap python-pip git-core gitk apache2 apache2-mpm-prefork apache2-utils libapache2-mod-python emacs nmap unzip make lvm2 build-essential mysql-client python-mysqldb libaio1 libncurses-dev libreadline-dev openssh-server openssh-blacklist openssh-blacklist-extra dnsmasq traceroute libreoffice imagemagick traceroute

   optional:
   sudo apt-get install keepass2

   sudo pip install -U pytz
   sudo pip install -U svglib

6. Setup Edgers PPA (for timely updates to X-Org and Nvidia Drivers)
    sudo apt-add-repository ppa:xorg-edgers/ppa
    sudo apt-get update
    sudo apt-get dist-upgrade

7. Set up VirtualBox PPA and install VirtualBox
   * wget -q http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc -O- | sudo apt-key add -
   * Using "Software Sources" add a "Additional repository" of:
           deb http://download.virtualbox.org/virtualbox/debian saucy contrib
   * sudo apt-get install virtualbox-4.3

8. Set up Node.js PPA and install node.js
   sudo apt-add-repository ppa:chris-lea/node.js
   sudo apt-get update
   sudo apt-get install nodejs

9. Set up hipchat
   echo "deb http://downloads.hipchat.com/linux/apt stable main" > /etc/apt/sources.list.d/atlassian-hipchat.list
   wget -O - https://www.hipchat.com/keys/hipchat-linux.key | apt-key add -
   apt-get update
   apt-get install hipchat

10. Wireless Settings for at work
   Need to connect to the "jupiter" Network. But Mint has a config issues when trying to use
   Network Manager.

   Go to Network Manager, Wireless. Pick jupiter
   Settings:
     * Security                                        : WPA & WPA2 Enterprise
     * Authentication (or EAP method)                  : Protected EAP (PEAP)
     * Anonymous Identity                              : <Leave Blank>
     * CA certificate                                  : <Leave Blank>
     * PEAP version                                    : Automatic
     * Inner authentication (or Phase 2 authentication): MSCHAPv2
     * Username                                        : Exxxxxx (twccorp EID)
     * Password                                        : <your mail password>

   You might get a "No certificate Authoritye certificate chosen" warning. Ignore it.


   For the issue on Mint, see: https://bugs.launchpad.net/linuxmint/+bug/1187483

   Edit the file:

       /etc/Network/Manager/system-connections/jupiter

   and remove the line in the [802-1x] section that says:

      system-ca-certs=true

   The file will then look like something like this:

      [ipv6]
      method=auto

      [connection]
      id=jupiter
      uuid=f9df691e-e9b4-4699-878f-03a0624f9b06
      type=802-11-wireless

      [802-11-wireless-security]
      key-mgmt=wpa-eap

      [802-11-wireless]
      ssid=jupiter
      mode=infrastructure
      mac-address=E0:9D:31:2B:89:34
      security=802-11-wireless-security

      [802-1x]
      eap=peap;
      identity=<YOUR EID here>
      phase2-auth=mschapv2
      password-flags=1

      [ipv4]
      method=auto

   Joe's config for Ubuntu/Xubuntu has similar issues:

      [ipv6]
      method=auto

      [connection]
      id=jupiter
      uuid=9f2890ad-5ae1-4401-b199-9c30cc5e9681
      type=802-11-wireless
      timestamp=1391011307

      [802-11-wireless-security]
      key-mgmt=wpa-eap

      [802-11-wireless]
      ssid=jupiter
      mode=infrastructure
      mac-address=68:94:23:3F:B0:E7
      security=802-11-wireless-security

      [802-1x]
      eap=peap;
      identity=<Your EID here>
      phase2-auth=mschapv2
      password=nopenopenopenope

      [ipv4]
      method=auto

11. Dynamic DNS settings
    See https://22.192.32.38/projects/process/wiki/DnsSettings

11. Install Oracle client and CX Oracle library
   * wget http://22.208.9.55/desktop_files/oracle-instantclient-11.2.0.1.0-linux-64.tar.gz
   * tar zxf oracle-instantclient-11.2.0.1.0-linux-64.tar.gz
   * rm oracle-instantclient-11.2.0.1.0-linux-64.tar.gz
   * cd instantclient_11_2/
   * ln -fs libclntsh.so.11.1 libclntsh.so
   * ln -fs libocci.so.11.1 libocci.so
   * mkdir -p network/admin
   * cd network/admin
   * scp rnd@22.208.14.43:/u01/app/oracle/product/9.2.0/network/admin/tnsnames.ora .
     * Had to modify all 10.x addresses to 22.x
   * echo -e "/home/rternosky/instantclient_11_2" >oracle-11.2.0.conf
      * sudo mv oracle-11.2.0.conf /etc/ld.so.conf.d/
      * sudo chown root.root /etc/ld.so.conf.d/oracle-11.2.0.conf
      * sudo /sbin/ldconfig
      * sudo ORACLE_HOME=/home/rternosky/instantclient_11_2/ pip install cx_oracle
      * export ORACLE_HOME=/home/rternosky/instantclient_11_2
      * $ORACLE_HOME/sqlplus corp@crprd
      * [enter password]
      * CTRL+D
      * python
      * >>> import cx_Oracle
      * CTRL+D

12. Setup yasql
   sudo su -
       * cpan DBI DBD::Oracle Term::ReadLine::Gnu Term::ReadKey Text::CSV_XS Time::HiRes
           Would you like to configure as much as possible automatically? [yes] => Hit Enter
           What approach do you want?  (Choose 'local::lib', 'sudo' or 'manual') [local::lib]  => Hit Enter
           Would you like me to automatically choose some CPAN mirror sites for you? ... [yes] => Hit Enter

           CPAN will do a TON of work building/installing perl modules
           BUT, if you look closely, the Oracle install will fail.

      * cd /root/.cpan/build/DBD-Oracle-1.50-5ruZE3  (or whatever version is current..tab complete after DBD-Oracle)
      * export ORACLE_HOME=/home/CHANGEME/instantclient_11_2
      * perl Makefile.PL
      * make
      * make install
      * tar xvf yasql-1.83.tar.gz
      * cd yasql-1.83
      * ./configure --prefix=/usr --sysconfdir=/etc
      * make
      * make install
      * cd ..
      * rm -rf yasql-1.83
      * rm -f yasql-1.8.3.tar
      * exit
      * cd
      * yasql corp@crprd
      * CTRL+D
      * rm -rf oradiag_rnd

13. Get our code from Github
   mkdir -p src/git
   cd src/git
   git clone git@github.com:Navisite/AjaxFramework
   git clone git@github.com:Navisite/billing-engine
   git clone git@github.com:Navisite/compliance
   git clone git@github.com:Navisite/configure
   git clone git@github.com:Navisite/corp_tools
   git clone git@github.com:Navisite/creditcard-engine
   git clone git@github.com:Navisite/einvoice-engine
   git clone git@github.com:Navisite/extranet
   git clone git@github.com:Navisite/feed-engine
   git clone git@github.com:Navisite/jquery
   git clone git@github.com:Navisite/legacy_naviweb
   git clone git@github.com:Navisite/MPS
   git clone git@github.com:Navisite/navisite
   git clone git@github.com:Navisite/portal
   git clone git@github.com:Navisite/pyxuss
   git clone git@github.com:Navisite/quote_api
   git clone git@github.com:Navisite/quote-engine
   git clone git@github.com:Navisite/quote_tool
   git clone git@github.com:Navisite/rnd_docs
   git clone git@github.com:Navisite/skeleton_project
   git clone git@github.com:Navisite/sqlapi
   git clone git@github.com:Navisite/sqldbi
   git clone git@github.com:Navisite/usage_feeds

14. Setup Monitors/Video


X. Printers

Y. VPN
   See http://10.192.32.22/projects/cloud/wiki/TWC_VPN
   1) Install Symantec VIP Access on your phone from an App Store
   2) Run the Symantec VIP Access app on your phone it will contain two pieces of infomration:
      A) Credential ID
      B) Security Code
   3) Register your phone on the following website:
      https://pvision.twcable.com:8233/vipssp
         Login with EID/password
      Use the Credential ID/Security Code on your phone for registration
   4) Install VPN software
      sudo apt-get install network-manager-openconnect vpnc openconnect network-manager-openconnect-gnome
   5) Add a VPN
      A) Run "Network Connections"
      B) Click the "Add" button
      C) Select a "connection type" of "VPN -> Cisoc AnyConnect Compatible VPN (openconnect)" and click "Create"
      D) Configure VPN settings:
         Change Name to TWC
         Gateway                          : cdc-era.twcable.com
         CA Certificate                   : <Leave Blank>
         Proxy                            : <Leave Blank>
         Allow Cisco Secure Desktop Trojan: Check the checkbox
         CSD Wrapper Script               : <Leave Blank>
         Certificate Authentication       : <Leave both options blank>
         Use FSID for key passphrase      : Leave unchecked

         Click Save
    6) Using VPN
       Go to Networking
       Select TWC VPN (instead of Wired/Wireless)
       Set it to ON
       click the weird button to right of VPN host
           GROUP   : Employee
           Username: Exxxxx
           Password: Your Email Password + 6 digit code from VIP Access App on your phone
       Press "Login" button

Z. Bring over old box data

AA. Dropbox
BB. Sloppy Mouse Focus
CC. NumPad ENTER key -> terminal
