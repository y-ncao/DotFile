# Old New Server Permission Setting(obsoleted)
(Keeping it to save all the old memories 😁)

1. Edit /etc/login.defs to have these values:

```
SYSLOG_SU_ENAB          yes
SYSLOG_SG_ENAB          yes
PASS_MAX_DAYS           90
PASS_MIN_DAYS           1
PASS_WARN_AGE           10
LOGIN_RETRIES           5
LOGIN_TIMEOUT           60
```

2. Setup password complexity:
```
  sudo touch /etc/security/opasswd
  sudo chown root:root /etc/security/opasswd
  sudo chmod 600 /etc/security/opasswd
```

make the "password" lines in /etc/pam.d/common-password look like:
password required pam_cracklib.so retry=3 minlen=12 difok=4
password required pam_unix.so md5 remember=8 use_authtok

```
pam_cracklib.so means:
    Is the new password just the old password with the letters reversed ("password" vs. "drowssap") or rotated ("password" vs. "asswordp")?
    Does the new password only differ from the old one due to change of case ("password" vs. "Password")?
    Are at least some minimum number of characters in the new password not present in the old password?
           This is where the "difok" parameter comes into play.
   These are the same checks you get in the pam_unix module if you turn on the "obscure" flag, but since we're already using
   pam_cracklib we don't need to use "obscure"

retry=3 means:
   users get three chances to pick a good password before the passwd program aborts.

minlen=12 difok=4 means:
  that the smallest password a user could have is 8 characters, and that's only if they use all four character sets
    (upper, lower, numeric, non-alphanum). If lower case only, it would be 12 chars min.

pam_unix.so is the standard unix password crypt matching

remember=8 gets us the required password history depth of 8

use_authtok tells pam_unix to not bother doing any of its own internal password checks, which duplicate many of the
            checks in pam_cracklib, but instead accept the password that the user inputs after it's been thoroughly checked by pam_cracklib.
```

3. Add each user:
```
   adduser rternosky
   adduser ycao
   adduser jkolb
   adduser wschmarder
   - we'll add simon when he's back in office
```

4. Set initial passwords
```
   passwd rternosky
   passwd ycao
   passwd jkolb
   passwd wschmarder
```

5. Add each user to sudoers file
```
   EDITOR=vi visudo   & make contents:

   root       ALL=(ALL) ALL
   jkolb      ALL=(ALL) ALL
   rnd        ALL=(ALL) ALL
   rternosky  ALL=(ALL) ALL
   svogel     ALL=(ALL) ALL
   ycao       ALL=(ALL) ALL
   wschmarder ALL=(ALL) ALL
```

6. make the root password never expire - since there isn't one.
```
chage -M -1 root
```

7. Disable remote root logins
   Edit /etc/ssh/sshd_config and make sure this line exists:
      PermitRootLogin no

9. Validate logins before loggig out & that we can sudo
