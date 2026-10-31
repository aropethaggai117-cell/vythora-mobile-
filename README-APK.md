# Vythora AI: build the Android APK (Capacitor 8, Android 7 to 16)

The APK is built in the cloud by GitHub Actions, so you do not need Android Studio.
The app is the same web app, wrapped natively. No secret keys are inside it: only your public Supabase URL and anon key.
The Groq key stays on your Supabase server.

## Do these BEFORE building
1. Finish the server setup from AI-SETUP.md (Groq key, ai-setup.sql, deploy the `chat` function).
2. Supabase > Authentication > URL Configuration > Redirect URLs: add `com.vythora.ai://auth`
3. Supabase secret: `ALLOWED_ORIGINS` must include the app's origin. Run:
   `supabase secrets set ALLOWED_ORIGINS=https://USERNAME.github.io,https://localhost`
4. Google and Facebook providers: the callback stays `https://<project-ref>.supabase.co/auth/v1/callback` (nothing new).

## Build
1. Create a new GitHub repository, e.g. `vythora-android`. Upload everything in this folder, keeping the folders
   (`www/`, `scripts/`, `.github/workflows/`). Easiest from a computer's browser (drag the folders in).
2. Repo > Settings > Secrets and variables > Actions > **Variables** > New repository variable:
   `SB_URL` = your Supabase Project URL, `SB_KEY` = your anon (public) key. Never the service_role key.
3. Actions tab > "Build Vythora AI APK" > Run workflow. It takes about 10 minutes.
4. Open the finished run > Artifacts > `vythora-ai-apk`, download it, unzip it to get `app-debug.apk`.

## Install on the Redmi 14C
- Send `app-debug.apk` to the phone and open it. Allow "Install unknown apps" for the app you opened it from.
- Xiaomi/HyperOS may show a security scan or Play Protect warning. This is a personal debug build, signed with a debug key.
- App name: Vythora AI. Package: `com.vythora.ai`. Allow the microphone when Voice asks.

## Honest limits
- Not test-built by me: I had no network access to run the build. If a step fails, send me the red error line from the Actions log.
- Debug-signed APK: fine for your own phone, not for the Play Store (that needs your own release keystore).
- Google sign-in opens your phone's browser and returns to the app (Google blocks sign-in inside embedded views).
- Email confirmation links should return to the app; if they don't, confirm in the browser and then sign in normally.
- Voice uses the phone's native speech recognition through a plugin; it has not been tested on a device yet.
