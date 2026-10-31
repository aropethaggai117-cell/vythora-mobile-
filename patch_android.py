import re
p='android/app/src/main/AndroidManifest.xml'; t=open(p).read()
f='''
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="com.vythora.ai" android:host="auth" />
            </intent-filter>
'''
assert '</activity>' in t
if 'com.vythora.ai' not in t: t=t.replace('</activity>',f+'        </activity>',1)
t=t.replace('android:allowBackup="true"','android:allowBackup="false"')
open(p,'w').write(t); print('manifest patched')
