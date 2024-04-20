
```
django-lms-main
├─ .git
│  ├─ config
│  ├─ description
│  ├─ HEAD
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  └─ update.sample
│  ├─ info
│  │  └─ exclude
│  ├─ objects
│  │  ├─ info
│  │  └─ pack
│  └─ refs
│     ├─ heads
│     └─ tags
├─ .gitignore
├─ .vscode
│  └─ settings.json
├─ accounts
│  ├─ admin.py
│  ├─ api
│  │  ├─ permissions.py
│  │  ├─ serializers.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ apps.py
│  ├─ decorators.py
│  ├─ filters.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_auto_20200729_1825.py
│  │  ├─ 0003_auto_20200730_0740.py
│  │  ├─ 0004_auto_20200822_2238.py
│  │  ├─ 0005_auto_20200822_2246.py
│  │  ├─ 0006_auto_20200822_2308.py
│  │  ├─ 0007_auto_20200825_1248.py
│  │  ├─ 0008_auto_20200831_1315.py
│  │  ├─ 0009_auto_20200906_1403.py
│  │  ├─ 0010_auto_20210401_1718.py
│  │  ├─ 0011_auto_20210823_0825.py
│  │  ├─ 0012_auto_20230112_2238.py
│  │  ├─ 0013_alter_departmenthead_id_alter_parent_id_and_more.py
│  │  ├─ 0014_alter_user_managers.py
│  │  ├─ 0015_alter_user_managers.py
│  │  ├─ 0016_alter_user_managers.py
│  │  ├─ 0017_alter_departmenthead_options_alter_parent_options_and_more.py
│  │  ├─ 0018_rename_department_student_program.py
│  │  ├─ 0019_user_gender.py
│  │  ├─ 0020_user_capacity_alter_student_level_alter_user_gender.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ signals.py
│  ├─ tests
│  │  ├─ test_decorators.py
│  │  ├─ test_filters.py
│  │  └─ __init__.py
│  ├─ tests.pys
│  ├─ urls.py
│  ├─ validators.py
│  ├─ views.py
│  └─ __init__.py
├─ chatbot.py
├─ chatpdf1.py
├─ config
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ core
│  ├─ admin.py
│  ├─ api
│  │  ├─ permissions.py
│  │  ├─ serializers.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_auto_20200730_0746.py
│  │  ├─ 0003_auto_20200730_0756.py
│  │  ├─ 0004_alter_newsandevents_id_alter_semester_id_and_more.py
│  │  ├─ 0005_activitylog.py
│  │  ├─ 0006_alter_semester_semester.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ course
│  ├─ admin.py
│  ├─ api
│  │  ├─ permissions.py
│  │  ├─ serializers.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ apps.py
│  ├─ decorators.py
│  ├─ filters.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_uploadvideo.py
│  │  ├─ 0003_auto_20200803_1335.py
│  │  ├─ 0004_auto_20200822_2238.py
│  │  ├─ 0005_alter_course_id_alter_courseallocation_id_and_more.py
│  │  ├─ 0006_courseoffer.py
│  │  ├─ 0007_alter_upload_file_alter_uploadvideo_video.py
│  │  ├─ 0008_course_order_weight_course_pincode_and_more.py
│  │  ├─ 0009_alter_course_code_alter_course_credit_and_more.py
│  │  ├─ 0010_remove_course_order_weight_remove_course_pincode_and_more.py
│  │  ├─ 0011_alter_course_code_alter_course_credit_and_more.py
│  │  ├─ 0012_alter_course_semester.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ utils.py
│  ├─ views.py
│  └─ __init__.py
├─ faiss_index
│  ├─ index.faiss
│  └─ index.pkl
├─ locale
│  └─ es
│     └─ LC_MESSAGES
│        └─ django.po
├─ manage.py
├─ merge.py
├─ requirements
│  ├─ base.txt
│  ├─ local.txt
│  └─ production.txt
├─ requirements.txt
├─ scripts
│  ├─ generate_fake_accounts_data.py
│  ├─ generate_fake_core_data.py
│  ├─ generate_fake_data.py
│  └─ __init__.py
├─ search
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ templatetags
│  │  ├─ class_name.py
│  │  └─ __init__.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ static
│  ├─ chatbot-style.css
│  ├─ css
│  │  ├─ style.min.css
│  │  └─ style.min.css.map
│  ├─ fonts
│  │  ├─ rubik-v14-latin
│  │  │  ├─ rubik-v14-latin-300.eot
│  │  │  ├─ rubik-v14-latin-300.svg
│  │  │  ├─ rubik-v14-latin-300.ttf
│  │  │  ├─ rubik-v14-latin-300.woff
│  │  │  ├─ rubik-v14-latin-300.woff2
│  │  │  ├─ rubik-v14-latin-regular.eot
│  │  │  ├─ rubik-v14-latin-regular.svg
│  │  │  ├─ rubik-v14-latin-regular.ttf
│  │  │  ├─ rubik-v14-latin-regular.woff
│  │  │  └─ rubik-v14-latin-regular.woff2
│  │  └─ webfonts
│  │     ├─ fa-brands-400.eot
│  │     ├─ fa-brands-400.svg
│  │     ├─ fa-brands-400.ttf
│  │     ├─ fa-brands-400.woff
│  │     ├─ fa-brands-400.woff2
│  │     ├─ fa-regular-400.eot
│  │     ├─ fa-regular-400.svg
│  │     ├─ fa-regular-400.ttf
│  │     ├─ fa-regular-400.woff
│  │     ├─ fa-regular-400.woff2
│  │     ├─ fa-solid-900.eot
│  │     ├─ fa-solid-900.svg
│  │     ├─ fa-solid-900.ttf
│  │     ├─ fa-solid-900.woff
│  │     └─ fa-solid-900.woff2
│  ├─ img
│  │  ├─ brand-white.png
│  │  ├─ dj-lms-dashboard.png
│  │  ├─ dj-lms.png
│  │  ├─ dotted.jpg
│  │  └─ favicon.png
│  ├─ js
│  │  └─ main.js
│  ├─ scss
│  │  └─ style.scss
│  └─ vendor
│     ├─ bootstrap-5.3.2
│     │  ├─ css
│     │  │  ├─ bootstrap-grid.css
│     │  │  ├─ bootstrap-grid.css.map
│     │  │  ├─ bootstrap-grid.min.css
│     │  │  ├─ bootstrap-grid.min.css.map
│     │  │  ├─ bootstrap-grid.rtl.css
│     │  │  ├─ bootstrap-grid.rtl.css.map
│     │  │  ├─ bootstrap-grid.rtl.min.css
│     │  │  ├─ bootstrap-grid.rtl.min.css.map
│     │  │  ├─ bootstrap-reboot.css
│     │  │  ├─ bootstrap-reboot.css.map
│     │  │  ├─ bootstrap-reboot.min.css
│     │  │  ├─ bootstrap-reboot.min.css.map
│     │  │  ├─ bootstrap-reboot.rtl.css
│     │  │  ├─ bootstrap-reboot.rtl.css.map
│     │  │  ├─ bootstrap-reboot.rtl.min.css
│     │  │  ├─ bootstrap-reboot.rtl.min.css.map
│     │  │  ├─ bootstrap-utilities.css
│     │  │  ├─ bootstrap-utilities.css.map
│     │  │  ├─ bootstrap-utilities.min.css
│     │  │  ├─ bootstrap-utilities.min.css.map
│     │  │  ├─ bootstrap-utilities.rtl.css
│     │  │  ├─ bootstrap-utilities.rtl.css.map
│     │  │  ├─ bootstrap-utilities.rtl.min.css
│     │  │  ├─ bootstrap-utilities.rtl.min.css.map
│     │  │  ├─ bootstrap.css
│     │  │  ├─ bootstrap.css.map
│     │  │  ├─ bootstrap.min.css
│     │  │  ├─ bootstrap.min.css.map
│     │  │  ├─ bootstrap.rtl.css
│     │  │  ├─ bootstrap.rtl.css.map
│     │  │  ├─ bootstrap.rtl.min.css
│     │  │  └─ bootstrap.rtl.min.css.map
│     │  └─ js
│     │     ├─ bootstrap.bundle.js
│     │     ├─ bootstrap.bundle.js.map
│     │     ├─ bootstrap.bundle.min.js
│     │     ├─ bootstrap.bundle.min.js.map
│     │     ├─ bootstrap.esm.js
│     │     ├─ bootstrap.esm.js.map
│     │     ├─ bootstrap.esm.min.js
│     │     ├─ bootstrap.esm.min.js.map
│     │     ├─ bootstrap.js
│     │     ├─ bootstrap.js.map
│     │     ├─ bootstrap.min.js
│     │     └─ bootstrap.min.js.map
│     ├─ fontawesome-6.5.1
│     │  ├─ css
│     │  │  ├─ all.css
│     │  │  ├─ all.min.css
│     │  │  ├─ brands.css
│     │  │  ├─ brands.min.css
│     │  │  ├─ fontawesome.css
│     │  │  ├─ fontawesome.min.css
│     │  │  ├─ regular.css
│     │  │  ├─ regular.min.css
│     │  │  ├─ solid.css
│     │  │  ├─ solid.min.css
│     │  │  ├─ svg-with-js.css
│     │  │  ├─ svg-with-js.min.css
│     │  │  ├─ v4-font-face.css
│     │  │  ├─ v4-font-face.min.css
│     │  │  ├─ v4-shims.css
│     │  │  ├─ v4-shims.min.css
│     │  │  ├─ v5-font-face.css
│     │  │  └─ v5-font-face.min.css
│     │  ├─ js
│     │  │  ├─ all.js
│     │  │  ├─ all.min.js
│     │  │  ├─ brands.js
│     │  │  ├─ brands.min.js
│     │  │  ├─ conflict-detection.js
│     │  │  ├─ conflict-detection.min.js
│     │  │  ├─ fontawesome.js
│     │  │  ├─ fontawesome.min.js
│     │  │  ├─ regular.js
│     │  │  ├─ regular.min.js
│     │  │  ├─ solid.js
│     │  │  ├─ solid.min.js
│     │  │  ├─ v4-shims.js
│     │  │  └─ v4-shims.min.js
│     │  ├─ less
│     │  │  ├─ brands.less
│     │  │  ├─ fontawesome.less
│     │  │  ├─ regular.less
│     │  │  ├─ solid.less
│     │  │  ├─ v4-shims.less
│     │  │  ├─ _animated.less
│     │  │  ├─ _bordered-pulled.less
│     │  │  ├─ _core.less
│     │  │  ├─ _fixed-width.less
│     │  │  ├─ _icons.less
│     │  │  ├─ _list.less
│     │  │  ├─ _mixins.less
│     │  │  ├─ _rotated-flipped.less
│     │  │  ├─ _screen-reader.less
│     │  │  ├─ _shims.less
│     │  │  ├─ _sizing.less
│     │  │  ├─ _stacked.less
│     │  │  └─ _variables.less
│     │  ├─ LICENSE.txt
│     │  ├─ metadata
│     │  │  ├─ categories.yml
│     │  │  ├─ icon-families.json
│     │  │  ├─ icon-families.yml
│     │  │  ├─ icons.json
│     │  │  ├─ icons.yml
│     │  │  ├─ shims.json
│     │  │  ├─ shims.yml
│     │  │  └─ sponsors.yml
│     │  ├─ scss
│     │  │  ├─ brands.scss
│     │  │  ├─ fontawesome.scss
│     │  │  ├─ regular.scss
│     │  │  ├─ solid.scss
│     │  │  ├─ v4-shims.scss
│     │  │  ├─ _animated.scss
│     │  │  ├─ _bordered-pulled.scss
│     │  │  ├─ _core.scss
│     │  │  ├─ _fixed-width.scss
│     │  │  ├─ _functions.scss
│     │  │  ├─ _icons.scss
│     │  │  ├─ _list.scss
│     │  │  ├─ _mixins.scss
│     │  │  ├─ _rotated-flipped.scss
│     │  │  ├─ _screen-reader.scss
│     │  │  ├─ _shims.scss
│     │  │  ├─ _sizing.scss
│     │  │  ├─ _stacked.scss
│     │  │  └─ _variables.scss
│     │  ├─ sprites
│     │  │  ├─ brands.svg
│     │  │  ├─ regular.svg
│     │  │  └─ solid.svg
│     │  ├─ svgs
│     │  │  ├─ brands
│     │  │  │  ├─ 42-group.svg
│     │  │  │  ├─ 500px.svg
│     │  │  │  ├─ accessible-icon.svg
│     │  │  │  ├─ accusoft.svg
│     │  │  │  ├─ adn.svg
│     │  │  │  ├─ adversal.svg
│     │  │  │  ├─ affiliatetheme.svg
│     │  │  │  ├─ airbnb.svg
│     │  │  │  ├─ algolia.svg
│     │  │  │  ├─ alipay.svg
│     │  │  │  ├─ amazon-pay.svg
│     │  │  │  ├─ amazon.svg
│     │  │  │  ├─ amilia.svg
│     │  │  │  ├─ android.svg
│     │  │  │  ├─ angellist.svg
│     │  │  │  ├─ angrycreative.svg
│     │  │  │  ├─ angular.svg
│     │  │  │  ├─ app-store-ios.svg
│     │  │  │  ├─ app-store.svg
│     │  │  │  ├─ apper.svg
│     │  │  │  ├─ apple-pay.svg
│     │  │  │  ├─ apple.svg
│     │  │  │  ├─ artstation.svg
│     │  │  │  ├─ asymmetrik.svg
│     │  │  │  ├─ atlassian.svg
│     │  │  │  ├─ audible.svg
│     │  │  │  ├─ autoprefixer.svg
│     │  │  │  ├─ avianex.svg
│     │  │  │  ├─ aviato.svg
│     │  │  │  ├─ aws.svg
│     │  │  │  ├─ bandcamp.svg
│     │  │  │  ├─ battle-net.svg
│     │  │  │  ├─ behance.svg
│     │  │  │  ├─ bilibili.svg
│     │  │  │  ├─ bimobject.svg
│     │  │  │  ├─ bitbucket.svg
│     │  │  │  ├─ bitcoin.svg
│     │  │  │  ├─ bity.svg
│     │  │  │  ├─ black-tie.svg
│     │  │  │  ├─ blackberry.svg
│     │  │  │  ├─ blogger-b.svg
│     │  │  │  ├─ blogger.svg
│     │  │  │  ├─ bluetooth-b.svg
│     │  │  │  ├─ bluetooth.svg
│     │  │  │  ├─ bootstrap.svg
│     │  │  │  ├─ bots.svg
│     │  │  │  ├─ brave-reverse.svg
│     │  │  │  ├─ brave.svg
│     │  │  │  ├─ btc.svg
│     │  │  │  ├─ buffer.svg
│     │  │  │  ├─ buromobelexperte.svg
│     │  │  │  ├─ buy-n-large.svg
│     │  │  │  ├─ buysellads.svg
│     │  │  │  ├─ canadian-maple-leaf.svg
│     │  │  │  ├─ cc-amazon-pay.svg
│     │  │  │  ├─ cc-amex.svg
│     │  │  │  ├─ cc-apple-pay.svg
│     │  │  │  ├─ cc-diners-club.svg
│     │  │  │  ├─ cc-discover.svg
│     │  │  │  ├─ cc-jcb.svg
│     │  │  │  ├─ cc-mastercard.svg
│     │  │  │  ├─ cc-paypal.svg
│     │  │  │  ├─ cc-stripe.svg
│     │  │  │  ├─ cc-visa.svg
│     │  │  │  ├─ centercode.svg
│     │  │  │  ├─ centos.svg
│     │  │  │  ├─ chrome.svg
│     │  │  │  ├─ chromecast.svg
│     │  │  │  ├─ cloudflare.svg
│     │  │  │  ├─ cloudscale.svg
│     │  │  │  ├─ cloudsmith.svg
│     │  │  │  ├─ cloudversify.svg
│     │  │  │  ├─ cmplid.svg
│     │  │  │  ├─ codepen.svg
│     │  │  │  ├─ codiepie.svg
│     │  │  │  ├─ confluence.svg
│     │  │  │  ├─ connectdevelop.svg
│     │  │  │  ├─ contao.svg
│     │  │  │  ├─ cotton-bureau.svg
│     │  │  │  ├─ cpanel.svg
│     │  │  │  ├─ creative-commons-by.svg
│     │  │  │  ├─ creative-commons-nc-eu.svg
│     │  │  │  ├─ creative-commons-nc-jp.svg
│     │  │  │  ├─ creative-commons-nc.svg
│     │  │  │  ├─ creative-commons-nd.svg
│     │  │  │  ├─ creative-commons-pd-alt.svg
│     │  │  │  ├─ creative-commons-pd.svg
│     │  │  │  ├─ creative-commons-remix.svg
│     │  │  │  ├─ creative-commons-sa.svg
│     │  │  │  ├─ creative-commons-sampling-plus.svg
│     │  │  │  ├─ creative-commons-sampling.svg
│     │  │  │  ├─ creative-commons-share.svg
│     │  │  │  ├─ creative-commons-zero.svg
│     │  │  │  ├─ creative-commons.svg
│     │  │  │  ├─ critical-role.svg
│     │  │  │  ├─ css3-alt.svg
│     │  │  │  ├─ css3.svg
│     │  │  │  ├─ cuttlefish.svg
│     │  │  │  ├─ d-and-d-beyond.svg
│     │  │  │  ├─ d-and-d.svg
│     │  │  │  ├─ dailymotion.svg
│     │  │  │  ├─ dashcube.svg
│     │  │  │  ├─ debian.svg
│     │  │  │  ├─ deezer.svg
│     │  │  │  ├─ delicious.svg
│     │  │  │  ├─ deploydog.svg
│     │  │  │  ├─ deskpro.svg
│     │  │  │  ├─ dev.svg
│     │  │  │  ├─ deviantart.svg
│     │  │  │  ├─ dhl.svg
│     │  │  │  ├─ diaspora.svg
│     │  │  │  ├─ digg.svg
│     │  │  │  ├─ digital-ocean.svg
│     │  │  │  ├─ discord.svg
│     │  │  │  ├─ discourse.svg
│     │  │  │  ├─ dochub.svg
│     │  │  │  ├─ docker.svg
│     │  │  │  ├─ draft2digital.svg
│     │  │  │  ├─ dribbble.svg
│     │  │  │  ├─ dropbox.svg
│     │  │  │  ├─ drupal.svg
│     │  │  │  ├─ dyalog.svg
│     │  │  │  ├─ earlybirds.svg
│     │  │  │  ├─ ebay.svg
│     │  │  │  ├─ edge-legacy.svg
│     │  │  │  ├─ edge.svg
│     │  │  │  ├─ elementor.svg
│     │  │  │  ├─ ello.svg
│     │  │  │  ├─ ember.svg
│     │  │  │  ├─ empire.svg
│     │  │  │  ├─ envira.svg
│     │  │  │  ├─ erlang.svg
│     │  │  │  ├─ ethereum.svg
│     │  │  │  ├─ etsy.svg
│     │  │  │  ├─ evernote.svg
│     │  │  │  ├─ expeditedssl.svg
│     │  │  │  ├─ facebook-f.svg
│     │  │  │  ├─ facebook-messenger.svg
│     │  │  │  ├─ facebook.svg
│     │  │  │  ├─ fantasy-flight-games.svg
│     │  │  │  ├─ fedex.svg
│     │  │  │  ├─ fedora.svg
│     │  │  │  ├─ figma.svg
│     │  │  │  ├─ firefox-browser.svg
│     │  │  │  ├─ firefox.svg
│     │  │  │  ├─ first-order-alt.svg
│     │  │  │  ├─ first-order.svg
│     │  │  │  ├─ firstdraft.svg
│     │  │  │  ├─ flickr.svg
│     │  │  │  ├─ flipboard.svg
│     │  │  │  ├─ fly.svg
│     │  │  │  ├─ font-awesome.svg
│     │  │  │  ├─ fonticons-fi.svg
│     │  │  │  ├─ fonticons.svg
│     │  │  │  ├─ fort-awesome-alt.svg
│     │  │  │  ├─ fort-awesome.svg
│     │  │  │  ├─ forumbee.svg
│     │  │  │  ├─ foursquare.svg
│     │  │  │  ├─ free-code-camp.svg
│     │  │  │  ├─ freebsd.svg
│     │  │  │  ├─ fulcrum.svg
│     │  │  │  ├─ galactic-republic.svg
│     │  │  │  ├─ galactic-senate.svg
│     │  │  │  ├─ get-pocket.svg
│     │  │  │  ├─ gg-circle.svg
│     │  │  │  ├─ gg.svg
│     │  │  │  ├─ git-alt.svg
│     │  │  │  ├─ git.svg
│     │  │  │  ├─ github-alt.svg
│     │  │  │  ├─ github.svg
│     │  │  │  ├─ gitkraken.svg
│     │  │  │  ├─ gitlab.svg
│     │  │  │  ├─ gitter.svg
│     │  │  │  ├─ glide-g.svg
│     │  │  │  ├─ glide.svg
│     │  │  │  ├─ gofore.svg
│     │  │  │  ├─ golang.svg
│     │  │  │  ├─ goodreads-g.svg
│     │  │  │  ├─ goodreads.svg
│     │  │  │  ├─ google-drive.svg
│     │  │  │  ├─ google-pay.svg
│     │  │  │  ├─ google-play.svg
│     │  │  │  ├─ google-plus-g.svg
│     │  │  │  ├─ google-plus.svg
│     │  │  │  ├─ google-scholar.svg
│     │  │  │  ├─ google-wallet.svg
│     │  │  │  ├─ google.svg
│     │  │  │  ├─ gratipay.svg
│     │  │  │  ├─ grav.svg
│     │  │  │  ├─ gripfire.svg
│     │  │  │  ├─ grunt.svg
│     │  │  │  ├─ guilded.svg
│     │  │  │  ├─ gulp.svg
│     │  │  │  ├─ hacker-news.svg
│     │  │  │  ├─ hackerrank.svg
│     │  │  │  ├─ hashnode.svg
│     │  │  │  ├─ hips.svg
│     │  │  │  ├─ hire-a-helper.svg
│     │  │  │  ├─ hive.svg
│     │  │  │  ├─ hooli.svg
│     │  │  │  ├─ hornbill.svg
│     │  │  │  ├─ hotjar.svg
│     │  │  │  ├─ houzz.svg
│     │  │  │  ├─ html5.svg
│     │  │  │  ├─ hubspot.svg
│     │  │  │  ├─ ideal.svg
│     │  │  │  ├─ imdb.svg
│     │  │  │  ├─ instagram.svg
│     │  │  │  ├─ instalod.svg
│     │  │  │  ├─ intercom.svg
│     │  │  │  ├─ internet-explorer.svg
│     │  │  │  ├─ invision.svg
│     │  │  │  ├─ ioxhost.svg
│     │  │  │  ├─ itch-io.svg
│     │  │  │  ├─ itunes-note.svg
│     │  │  │  ├─ itunes.svg
│     │  │  │  ├─ java.svg
│     │  │  │  ├─ jedi-order.svg
│     │  │  │  ├─ jenkins.svg
│     │  │  │  ├─ jira.svg
│     │  │  │  ├─ joget.svg
│     │  │  │  ├─ joomla.svg
│     │  │  │  ├─ js.svg
│     │  │  │  ├─ jsfiddle.svg
│     │  │  │  ├─ kaggle.svg
│     │  │  │  ├─ keybase.svg
│     │  │  │  ├─ keycdn.svg
│     │  │  │  ├─ kickstarter-k.svg
│     │  │  │  ├─ kickstarter.svg
│     │  │  │  ├─ korvue.svg
│     │  │  │  ├─ laravel.svg
│     │  │  │  ├─ lastfm.svg
│     │  │  │  ├─ leanpub.svg
│     │  │  │  ├─ less.svg
│     │  │  │  ├─ letterboxd.svg
│     │  │  │  ├─ line.svg
│     │  │  │  ├─ linkedin-in.svg
│     │  │  │  ├─ linkedin.svg
│     │  │  │  ├─ linode.svg
│     │  │  │  ├─ linux.svg
│     │  │  │  ├─ lyft.svg
│     │  │  │  ├─ magento.svg
│     │  │  │  ├─ mailchimp.svg
│     │  │  │  ├─ mandalorian.svg
│     │  │  │  ├─ markdown.svg
│     │  │  │  ├─ mastodon.svg
│     │  │  │  ├─ maxcdn.svg
│     │  │  │  ├─ mdb.svg
│     │  │  │  ├─ medapps.svg
│     │  │  │  ├─ medium.svg
│     │  │  │  ├─ medrt.svg
│     │  │  │  ├─ meetup.svg
│     │  │  │  ├─ megaport.svg
│     │  │  │  ├─ mendeley.svg
│     │  │  │  ├─ meta.svg
│     │  │  │  ├─ microblog.svg
│     │  │  │  ├─ microsoft.svg
│     │  │  │  ├─ mintbit.svg
│     │  │  │  ├─ mix.svg
│     │  │  │  ├─ mixcloud.svg
│     │  │  │  ├─ mixer.svg
│     │  │  │  ├─ mizuni.svg
│     │  │  │  ├─ modx.svg
│     │  │  │  ├─ monero.svg
│     │  │  │  ├─ napster.svg
│     │  │  │  ├─ neos.svg
│     │  │  │  ├─ nfc-directional.svg
│     │  │  │  ├─ nfc-symbol.svg
│     │  │  │  ├─ nimblr.svg
│     │  │  │  ├─ node-js.svg
│     │  │  │  ├─ node.svg
│     │  │  │  ├─ npm.svg
│     │  │  │  ├─ ns8.svg
│     │  │  │  ├─ nutritionix.svg
│     │  │  │  ├─ octopus-deploy.svg
│     │  │  │  ├─ odnoklassniki.svg
│     │  │  │  ├─ odysee.svg
│     │  │  │  ├─ old-republic.svg
│     │  │  │  ├─ opencart.svg
│     │  │  │  ├─ openid.svg
│     │  │  │  ├─ opensuse.svg
│     │  │  │  ├─ opera.svg
│     │  │  │  ├─ optin-monster.svg
│     │  │  │  ├─ orcid.svg
│     │  │  │  ├─ osi.svg
│     │  │  │  ├─ padlet.svg
│     │  │  │  ├─ page4.svg
│     │  │  │  ├─ pagelines.svg
│     │  │  │  ├─ palfed.svg
│     │  │  │  ├─ patreon.svg
│     │  │  │  ├─ paypal.svg
│     │  │  │  ├─ perbyte.svg
│     │  │  │  ├─ periscope.svg
│     │  │  │  ├─ phabricator.svg
│     │  │  │  ├─ phoenix-framework.svg
│     │  │  │  ├─ phoenix-squadron.svg
│     │  │  │  ├─ php.svg
│     │  │  │  ├─ pied-piper-alt.svg
│     │  │  │  ├─ pied-piper-hat.svg
│     │  │  │  ├─ pied-piper-pp.svg
│     │  │  │  ├─ pied-piper.svg
│     │  │  │  ├─ pinterest-p.svg
│     │  │  │  ├─ pinterest.svg
│     │  │  │  ├─ pix.svg
│     │  │  │  ├─ pixiv.svg
│     │  │  │  ├─ playstation.svg
│     │  │  │  ├─ product-hunt.svg
│     │  │  │  ├─ pushed.svg
│     │  │  │  ├─ python.svg
│     │  │  │  ├─ qq.svg
│     │  │  │  ├─ quinscape.svg
│     │  │  │  ├─ quora.svg
│     │  │  │  ├─ r-project.svg
│     │  │  │  ├─ raspberry-pi.svg
│     │  │  │  ├─ ravelry.svg
│     │  │  │  ├─ react.svg
│     │  │  │  ├─ reacteurope.svg
│     │  │  │  ├─ readme.svg
│     │  │  │  ├─ rebel.svg
│     │  │  │  ├─ red-river.svg
│     │  │  │  ├─ reddit-alien.svg
│     │  │  │  ├─ reddit.svg
│     │  │  │  ├─ redhat.svg
│     │  │  │  ├─ renren.svg
│     │  │  │  ├─ replyd.svg
│     │  │  │  ├─ researchgate.svg
│     │  │  │  ├─ resolving.svg
│     │  │  │  ├─ rev.svg
│     │  │  │  ├─ rocketchat.svg
│     │  │  │  ├─ rockrms.svg
│     │  │  │  ├─ rust.svg
│     │  │  │  ├─ safari.svg
│     │  │  │  ├─ salesforce.svg
│     │  │  │  ├─ sass.svg
│     │  │  │  ├─ schlix.svg
│     │  │  │  ├─ screenpal.svg
│     │  │  │  ├─ scribd.svg
│     │  │  │  ├─ searchengin.svg
│     │  │  │  ├─ sellcast.svg
│     │  │  │  ├─ sellsy.svg
│     │  │  │  ├─ servicestack.svg
│     │  │  │  ├─ shirtsinbulk.svg
│     │  │  │  ├─ shoelace.svg
│     │  │  │  ├─ shopify.svg
│     │  │  │  ├─ shopware.svg
│     │  │  │  ├─ signal-messenger.svg
│     │  │  │  ├─ simplybuilt.svg
│     │  │  │  ├─ sistrix.svg
│     │  │  │  ├─ sith.svg
│     │  │  │  ├─ sitrox.svg
│     │  │  │  ├─ sketch.svg
│     │  │  │  ├─ skyatlas.svg
│     │  │  │  ├─ skype.svg
│     │  │  │  ├─ slack.svg
│     │  │  │  ├─ slideshare.svg
│     │  │  │  ├─ snapchat.svg
│     │  │  │  ├─ soundcloud.svg
│     │  │  │  ├─ sourcetree.svg
│     │  │  │  ├─ space-awesome.svg
│     │  │  │  ├─ speakap.svg
│     │  │  │  ├─ speaker-deck.svg
│     │  │  │  ├─ spotify.svg
│     │  │  │  ├─ square-behance.svg
│     │  │  │  ├─ square-dribbble.svg
│     │  │  │  ├─ square-facebook.svg
│     │  │  │  ├─ square-font-awesome-stroke.svg
│     │  │  │  ├─ square-font-awesome.svg
│     │  │  │  ├─ square-git.svg
│     │  │  │  ├─ square-github.svg
│     │  │  │  ├─ square-gitlab.svg
│     │  │  │  ├─ square-google-plus.svg
│     │  │  │  ├─ square-hacker-news.svg
│     │  │  │  ├─ square-instagram.svg
│     │  │  │  ├─ square-js.svg
│     │  │  │  ├─ square-lastfm.svg
│     │  │  │  ├─ square-letterboxd.svg
│     │  │  │  ├─ square-odnoklassniki.svg
│     │  │  │  ├─ square-pied-piper.svg
│     │  │  │  ├─ square-pinterest.svg
│     │  │  │  ├─ square-reddit.svg
│     │  │  │  ├─ square-snapchat.svg
│     │  │  │  ├─ square-steam.svg
│     │  │  │  ├─ square-threads.svg
│     │  │  │  ├─ square-tumblr.svg
│     │  │  │  ├─ square-twitter.svg
│     │  │  │  ├─ square-viadeo.svg
│     │  │  │  ├─ square-vimeo.svg
│     │  │  │  ├─ square-whatsapp.svg
│     │  │  │  ├─ square-x-twitter.svg
│     │  │  │  ├─ square-xing.svg
│     │  │  │  ├─ square-youtube.svg
│     │  │  │  ├─ squarespace.svg
│     │  │  │  ├─ stack-exchange.svg
│     │  │  │  ├─ stack-overflow.svg
│     │  │  │  ├─ stackpath.svg
│     │  │  │  ├─ staylinked.svg
│     │  │  │  ├─ steam-symbol.svg
│     │  │  │  ├─ steam.svg
│     │  │  │  ├─ sticker-mule.svg
│     │  │  │  ├─ strava.svg
│     │  │  │  ├─ stripe-s.svg
│     │  │  │  ├─ stripe.svg
│     │  │  │  ├─ stubber.svg
│     │  │  │  ├─ studiovinari.svg
│     │  │  │  ├─ stumbleupon-circle.svg
│     │  │  │  ├─ stumbleupon.svg
│     │  │  │  ├─ superpowers.svg
│     │  │  │  ├─ supple.svg
│     │  │  │  ├─ suse.svg
│     │  │  │  ├─ swift.svg
│     │  │  │  ├─ symfony.svg
│     │  │  │  ├─ teamspeak.svg
│     │  │  │  ├─ telegram.svg
│     │  │  │  ├─ tencent-weibo.svg
│     │  │  │  ├─ the-red-yeti.svg
│     │  │  │  ├─ themeco.svg
│     │  │  │  ├─ themeisle.svg
│     │  │  │  ├─ think-peaks.svg
│     │  │  │  ├─ threads.svg
│     │  │  │  ├─ tiktok.svg
│     │  │  │  ├─ trade-federation.svg
│     │  │  │  ├─ trello.svg
│     │  │  │  ├─ tumblr.svg
│     │  │  │  ├─ twitch.svg
│     │  │  │  ├─ twitter.svg
│     │  │  │  ├─ typo3.svg
│     │  │  │  ├─ uber.svg
│     │  │  │  ├─ ubuntu.svg
│     │  │  │  ├─ uikit.svg
│     │  │  │  ├─ umbraco.svg
│     │  │  │  ├─ uncharted.svg
│     │  │  │  ├─ uniregistry.svg
│     │  │  │  ├─ unity.svg
│     │  │  │  ├─ unsplash.svg
│     │  │  │  ├─ untappd.svg
│     │  │  │  ├─ ups.svg
│     │  │  │  ├─ upwork.svg
│     │  │  │  ├─ usb.svg
│     │  │  │  ├─ usps.svg
│     │  │  │  ├─ ussunnah.svg
│     │  │  │  ├─ vaadin.svg
│     │  │  │  ├─ viacoin.svg
│     │  │  │  ├─ viadeo.svg
│     │  │  │  ├─ viber.svg
│     │  │  │  ├─ vimeo-v.svg
│     │  │  │  ├─ vimeo.svg
│     │  │  │  ├─ vine.svg
│     │  │  │  ├─ vk.svg
│     │  │  │  ├─ vnv.svg
│     │  │  │  ├─ vuejs.svg
│     │  │  │  ├─ watchman-monitoring.svg
│     │  │  │  ├─ waze.svg
│     │  │  │  ├─ webflow.svg
│     │  │  │  ├─ weebly.svg
│     │  │  │  ├─ weibo.svg
│     │  │  │  ├─ weixin.svg
│     │  │  │  ├─ whatsapp.svg
│     │  │  │  ├─ whmcs.svg
│     │  │  │  ├─ wikipedia-w.svg
│     │  │  │  ├─ windows.svg
│     │  │  │  ├─ wirsindhandwerk.svg
│     │  │  │  ├─ wix.svg
│     │  │  │  ├─ wizards-of-the-coast.svg
│     │  │  │  ├─ wodu.svg
│     │  │  │  ├─ wolf-pack-battalion.svg
│     │  │  │  ├─ wordpress-simple.svg
│     │  │  │  ├─ wordpress.svg
│     │  │  │  ├─ wpbeginner.svg
│     │  │  │  ├─ wpexplorer.svg
│     │  │  │  ├─ wpforms.svg
│     │  │  │  ├─ wpressr.svg
│     │  │  │  ├─ x-twitter.svg
│     │  │  │  ├─ xbox.svg
│     │  │  │  ├─ xing.svg
│     │  │  │  ├─ y-combinator.svg
│     │  │  │  ├─ yahoo.svg
│     │  │  │  ├─ yammer.svg
│     │  │  │  ├─ yandex-international.svg
│     │  │  │  ├─ yandex.svg
│     │  │  │  ├─ yarn.svg
│     │  │  │  ├─ yelp.svg
│     │  │  │  ├─ yoast.svg
│     │  │  │  ├─ youtube.svg
│     │  │  │  └─ zhihu.svg
│     │  │  ├─ regular
│     │  │  │  ├─ address-book.svg
│     │  │  │  ├─ address-card.svg
│     │  │  │  ├─ bell-slash.svg
│     │  │  │  ├─ bell.svg
│     │  │  │  ├─ bookmark.svg
│     │  │  │  ├─ building.svg
│     │  │  │  ├─ calendar-check.svg
│     │  │  │  ├─ calendar-days.svg
│     │  │  │  ├─ calendar-minus.svg
│     │  │  │  ├─ calendar-plus.svg
│     │  │  │  ├─ calendar-xmark.svg
│     │  │  │  ├─ calendar.svg
│     │  │  │  ├─ chart-bar.svg
│     │  │  │  ├─ chess-bishop.svg
│     │  │  │  ├─ chess-king.svg
│     │  │  │  ├─ chess-knight.svg
│     │  │  │  ├─ chess-pawn.svg
│     │  │  │  ├─ chess-queen.svg
│     │  │  │  ├─ chess-rook.svg
│     │  │  │  ├─ circle-check.svg
│     │  │  │  ├─ circle-dot.svg
│     │  │  │  ├─ circle-down.svg
│     │  │  │  ├─ circle-left.svg
│     │  │  │  ├─ circle-pause.svg
│     │  │  │  ├─ circle-play.svg
│     │  │  │  ├─ circle-question.svg
│     │  │  │  ├─ circle-right.svg
│     │  │  │  ├─ circle-stop.svg
│     │  │  │  ├─ circle-up.svg
│     │  │  │  ├─ circle-user.svg
│     │  │  │  ├─ circle-xmark.svg
│     │  │  │  ├─ circle.svg
│     │  │  │  ├─ clipboard.svg
│     │  │  │  ├─ clock.svg
│     │  │  │  ├─ clone.svg
│     │  │  │  ├─ closed-captioning.svg
│     │  │  │  ├─ comment-dots.svg
│     │  │  │  ├─ comment.svg
│     │  │  │  ├─ comments.svg
│     │  │  │  ├─ compass.svg
│     │  │  │  ├─ copy.svg
│     │  │  │  ├─ copyright.svg
│     │  │  │  ├─ credit-card.svg
│     │  │  │  ├─ envelope-open.svg
│     │  │  │  ├─ envelope.svg
│     │  │  │  ├─ eye-slash.svg
│     │  │  │  ├─ eye.svg
│     │  │  │  ├─ face-angry.svg
│     │  │  │  ├─ face-dizzy.svg
│     │  │  │  ├─ face-flushed.svg
│     │  │  │  ├─ face-frown-open.svg
│     │  │  │  ├─ face-frown.svg
│     │  │  │  ├─ face-grimace.svg
│     │  │  │  ├─ face-grin-beam-sweat.svg
│     │  │  │  ├─ face-grin-beam.svg
│     │  │  │  ├─ face-grin-hearts.svg
│     │  │  │  ├─ face-grin-squint-tears.svg
│     │  │  │  ├─ face-grin-squint.svg
│     │  │  │  ├─ face-grin-stars.svg
│     │  │  │  ├─ face-grin-tears.svg
│     │  │  │  ├─ face-grin-tongue-squint.svg
│     │  │  │  ├─ face-grin-tongue-wink.svg
│     │  │  │  ├─ face-grin-tongue.svg
│     │  │  │  ├─ face-grin-wide.svg
│     │  │  │  ├─ face-grin-wink.svg
│     │  │  │  ├─ face-grin.svg
│     │  │  │  ├─ face-kiss-beam.svg
│     │  │  │  ├─ face-kiss-wink-heart.svg
│     │  │  │  ├─ face-kiss.svg
│     │  │  │  ├─ face-laugh-beam.svg
│     │  │  │  ├─ face-laugh-squint.svg
│     │  │  │  ├─ face-laugh-wink.svg
│     │  │  │  ├─ face-laugh.svg
│     │  │  │  ├─ face-meh-blank.svg
│     │  │  │  ├─ face-meh.svg
│     │  │  │  ├─ face-rolling-eyes.svg
│     │  │  │  ├─ face-sad-cry.svg
│     │  │  │  ├─ face-sad-tear.svg
│     │  │  │  ├─ face-smile-beam.svg
│     │  │  │  ├─ face-smile-wink.svg
│     │  │  │  ├─ face-smile.svg
│     │  │  │  ├─ face-surprise.svg
│     │  │  │  ├─ face-tired.svg
│     │  │  │  ├─ file-audio.svg
│     │  │  │  ├─ file-code.svg
│     │  │  │  ├─ file-excel.svg
│     │  │  │  ├─ file-image.svg
│     │  │  │  ├─ file-lines.svg
│     │  │  │  ├─ file-pdf.svg
│     │  │  │  ├─ file-powerpoint.svg
│     │  │  │  ├─ file-video.svg
│     │  │  │  ├─ file-word.svg
│     │  │  │  ├─ file-zipper.svg
│     │  │  │  ├─ file.svg
│     │  │  │  ├─ flag.svg
│     │  │  │  ├─ floppy-disk.svg
│     │  │  │  ├─ folder-closed.svg
│     │  │  │  ├─ folder-open.svg
│     │  │  │  ├─ folder.svg
│     │  │  │  ├─ font-awesome.svg
│     │  │  │  ├─ futbol.svg
│     │  │  │  ├─ gem.svg
│     │  │  │  ├─ hand-back-fist.svg
│     │  │  │  ├─ hand-lizard.svg
│     │  │  │  ├─ hand-peace.svg
│     │  │  │  ├─ hand-point-down.svg
│     │  │  │  ├─ hand-point-left.svg
│     │  │  │  ├─ hand-point-right.svg
│     │  │  │  ├─ hand-point-up.svg
│     │  │  │  ├─ hand-pointer.svg
│     │  │  │  ├─ hand-scissors.svg
│     │  │  │  ├─ hand-spock.svg
│     │  │  │  ├─ hand.svg
│     │  │  │  ├─ handshake.svg
│     │  │  │  ├─ hard-drive.svg
│     │  │  │  ├─ heart.svg
│     │  │  │  ├─ hospital.svg
│     │  │  │  ├─ hourglass-half.svg
│     │  │  │  ├─ hourglass.svg
│     │  │  │  ├─ id-badge.svg
│     │  │  │  ├─ id-card.svg
│     │  │  │  ├─ image.svg
│     │  │  │  ├─ images.svg
│     │  │  │  ├─ keyboard.svg
│     │  │  │  ├─ lemon.svg
│     │  │  │  ├─ life-ring.svg
│     │  │  │  ├─ lightbulb.svg
│     │  │  │  ├─ map.svg
│     │  │  │  ├─ message.svg
│     │  │  │  ├─ money-bill-1.svg
│     │  │  │  ├─ moon.svg
│     │  │  │  ├─ newspaper.svg
│     │  │  │  ├─ note-sticky.svg
│     │  │  │  ├─ object-group.svg
│     │  │  │  ├─ object-ungroup.svg
│     │  │  │  ├─ paper-plane.svg
│     │  │  │  ├─ paste.svg
│     │  │  │  ├─ pen-to-square.svg
│     │  │  │  ├─ rectangle-list.svg
│     │  │  │  ├─ rectangle-xmark.svg
│     │  │  │  ├─ registered.svg
│     │  │  │  ├─ share-from-square.svg
│     │  │  │  ├─ snowflake.svg
│     │  │  │  ├─ square-caret-down.svg
│     │  │  │  ├─ square-caret-left.svg
│     │  │  │  ├─ square-caret-right.svg
│     │  │  │  ├─ square-caret-up.svg
│     │  │  │  ├─ square-check.svg
│     │  │  │  ├─ square-full.svg
│     │  │  │  ├─ square-minus.svg
│     │  │  │  ├─ square-plus.svg
│     │  │  │  ├─ square.svg
│     │  │  │  ├─ star-half-stroke.svg
│     │  │  │  ├─ star-half.svg
│     │  │  │  ├─ star.svg
│     │  │  │  ├─ sun.svg
│     │  │  │  ├─ thumbs-down.svg
│     │  │  │  ├─ thumbs-up.svg
│     │  │  │  ├─ trash-can.svg
│     │  │  │  ├─ user.svg
│     │  │  │  ├─ window-maximize.svg
│     │  │  │  ├─ window-minimize.svg
│     │  │  │  └─ window-restore.svg
│     │  │  └─ solid
│     │  │     ├─ 0.svg
│     │  │     ├─ 1.svg
│     │  │     ├─ 2.svg
│     │  │     ├─ 3.svg
│     │  │     ├─ 4.svg
│     │  │     ├─ 5.svg
│     │  │     ├─ 6.svg
│     │  │     ├─ 7.svg
│     │  │     ├─ 8.svg
│     │  │     ├─ 9.svg
│     │  │     ├─ a.svg
│     │  │     ├─ address-book.svg
│     │  │     ├─ address-card.svg
│     │  │     ├─ align-center.svg
│     │  │     ├─ align-justify.svg
│     │  │     ├─ align-left.svg
│     │  │     ├─ align-right.svg
│     │  │     ├─ anchor-circle-check.svg
│     │  │     ├─ anchor-circle-exclamation.svg
│     │  │     ├─ anchor-circle-xmark.svg
│     │  │     ├─ anchor-lock.svg
│     │  │     ├─ anchor.svg
│     │  │     ├─ angle-down.svg
│     │  │     ├─ angle-left.svg
│     │  │     ├─ angle-right.svg
│     │  │     ├─ angle-up.svg
│     │  │     ├─ angles-down.svg
│     │  │     ├─ angles-left.svg
│     │  │     ├─ angles-right.svg
│     │  │     ├─ angles-up.svg
│     │  │     ├─ ankh.svg
│     │  │     ├─ apple-whole.svg
│     │  │     ├─ archway.svg
│     │  │     ├─ arrow-down-1-9.svg
│     │  │     ├─ arrow-down-9-1.svg
│     │  │     ├─ arrow-down-a-z.svg
│     │  │     ├─ arrow-down-long.svg
│     │  │     ├─ arrow-down-short-wide.svg
│     │  │     ├─ arrow-down-up-across-line.svg
│     │  │     ├─ arrow-down-up-lock.svg
│     │  │     ├─ arrow-down-wide-short.svg
│     │  │     ├─ arrow-down-z-a.svg
│     │  │     ├─ arrow-down.svg
│     │  │     ├─ arrow-left-long.svg
│     │  │     ├─ arrow-left.svg
│     │  │     ├─ arrow-pointer.svg
│     │  │     ├─ arrow-right-arrow-left.svg
│     │  │     ├─ arrow-right-from-bracket.svg
│     │  │     ├─ arrow-right-long.svg
│     │  │     ├─ arrow-right-to-bracket.svg
│     │  │     ├─ arrow-right-to-city.svg
│     │  │     ├─ arrow-right.svg
│     │  │     ├─ arrow-rotate-left.svg
│     │  │     ├─ arrow-rotate-right.svg
│     │  │     ├─ arrow-trend-down.svg
│     │  │     ├─ arrow-trend-up.svg
│     │  │     ├─ arrow-turn-down.svg
│     │  │     ├─ arrow-turn-up.svg
│     │  │     ├─ arrow-up-1-9.svg
│     │  │     ├─ arrow-up-9-1.svg
│     │  │     ├─ arrow-up-a-z.svg
│     │  │     ├─ arrow-up-from-bracket.svg
│     │  │     ├─ arrow-up-from-ground-water.svg
│     │  │     ├─ arrow-up-from-water-pump.svg
│     │  │     ├─ arrow-up-long.svg
│     │  │     ├─ arrow-up-right-dots.svg
│     │  │     ├─ arrow-up-right-from-square.svg
│     │  │     ├─ arrow-up-short-wide.svg
│     │  │     ├─ arrow-up-wide-short.svg
│     │  │     ├─ arrow-up-z-a.svg
│     │  │     ├─ arrow-up.svg
│     │  │     ├─ arrows-down-to-line.svg
│     │  │     ├─ arrows-down-to-people.svg
│     │  │     ├─ arrows-left-right-to-line.svg
│     │  │     ├─ arrows-left-right.svg
│     │  │     ├─ arrows-rotate.svg
│     │  │     ├─ arrows-spin.svg
│     │  │     ├─ arrows-split-up-and-left.svg
│     │  │     ├─ arrows-to-circle.svg
│     │  │     ├─ arrows-to-dot.svg
│     │  │     ├─ arrows-to-eye.svg
│     │  │     ├─ arrows-turn-right.svg
│     │  │     ├─ arrows-turn-to-dots.svg
│     │  │     ├─ arrows-up-down-left-right.svg
│     │  │     ├─ arrows-up-down.svg
│     │  │     ├─ arrows-up-to-line.svg
│     │  │     ├─ asterisk.svg
│     │  │     ├─ at.svg
│     │  │     ├─ atom.svg
│     │  │     ├─ audio-description.svg
│     │  │     ├─ austral-sign.svg
│     │  │     ├─ award.svg
│     │  │     ├─ b.svg
│     │  │     ├─ baby-carriage.svg
│     │  │     ├─ baby.svg
│     │  │     ├─ backward-fast.svg
│     │  │     ├─ backward-step.svg
│     │  │     ├─ backward.svg
│     │  │     ├─ bacon.svg
│     │  │     ├─ bacteria.svg
│     │  │     ├─ bacterium.svg
│     │  │     ├─ bag-shopping.svg
│     │  │     ├─ bahai.svg
│     │  │     ├─ baht-sign.svg
│     │  │     ├─ ban-smoking.svg
│     │  │     ├─ ban.svg
│     │  │     ├─ bandage.svg
│     │  │     ├─ bangladeshi-taka-sign.svg
│     │  │     ├─ barcode.svg
│     │  │     ├─ bars-progress.svg
│     │  │     ├─ bars-staggered.svg
│     │  │     ├─ bars.svg
│     │  │     ├─ baseball-bat-ball.svg
│     │  │     ├─ baseball.svg
│     │  │     ├─ basket-shopping.svg
│     │  │     ├─ basketball.svg
│     │  │     ├─ bath.svg
│     │  │     ├─ battery-empty.svg
│     │  │     ├─ battery-full.svg
│     │  │     ├─ battery-half.svg
│     │  │     ├─ battery-quarter.svg
│     │  │     ├─ battery-three-quarters.svg
│     │  │     ├─ bed-pulse.svg
│     │  │     ├─ bed.svg
│     │  │     ├─ beer-mug-empty.svg
│     │  │     ├─ bell-concierge.svg
│     │  │     ├─ bell-slash.svg
│     │  │     ├─ bell.svg
│     │  │     ├─ bezier-curve.svg
│     │  │     ├─ bicycle.svg
│     │  │     ├─ binoculars.svg
│     │  │     ├─ biohazard.svg
│     │  │     ├─ bitcoin-sign.svg
│     │  │     ├─ blender-phone.svg
│     │  │     ├─ blender.svg
│     │  │     ├─ blog.svg
│     │  │     ├─ bold.svg
│     │  │     ├─ bolt-lightning.svg
│     │  │     ├─ bolt.svg
│     │  │     ├─ bomb.svg
│     │  │     ├─ bone.svg
│     │  │     ├─ bong.svg
│     │  │     ├─ book-atlas.svg
│     │  │     ├─ book-bible.svg
│     │  │     ├─ book-bookmark.svg
│     │  │     ├─ book-journal-whills.svg
│     │  │     ├─ book-medical.svg
│     │  │     ├─ book-open-reader.svg
│     │  │     ├─ book-open.svg
│     │  │     ├─ book-quran.svg
│     │  │     ├─ book-skull.svg
│     │  │     ├─ book-tanakh.svg
│     │  │     ├─ book.svg
│     │  │     ├─ bookmark.svg
│     │  │     ├─ border-all.svg
│     │  │     ├─ border-none.svg
│     │  │     ├─ border-top-left.svg
│     │  │     ├─ bore-hole.svg
│     │  │     ├─ bottle-droplet.svg
│     │  │     ├─ bottle-water.svg
│     │  │     ├─ bowl-food.svg
│     │  │     ├─ bowl-rice.svg
│     │  │     ├─ bowling-ball.svg
│     │  │     ├─ box-archive.svg
│     │  │     ├─ box-open.svg
│     │  │     ├─ box-tissue.svg
│     │  │     ├─ box.svg
│     │  │     ├─ boxes-packing.svg
│     │  │     ├─ boxes-stacked.svg
│     │  │     ├─ braille.svg
│     │  │     ├─ brain.svg
│     │  │     ├─ brazilian-real-sign.svg
│     │  │     ├─ bread-slice.svg
│     │  │     ├─ bridge-circle-check.svg
│     │  │     ├─ bridge-circle-exclamation.svg
│     │  │     ├─ bridge-circle-xmark.svg
│     │  │     ├─ bridge-lock.svg
│     │  │     ├─ bridge-water.svg
│     │  │     ├─ bridge.svg
│     │  │     ├─ briefcase-medical.svg
│     │  │     ├─ briefcase.svg
│     │  │     ├─ broom-ball.svg
│     │  │     ├─ broom.svg
│     │  │     ├─ brush.svg
│     │  │     ├─ bucket.svg
│     │  │     ├─ bug-slash.svg
│     │  │     ├─ bug.svg
│     │  │     ├─ bugs.svg
│     │  │     ├─ building-circle-arrow-right.svg
│     │  │     ├─ building-circle-check.svg
│     │  │     ├─ building-circle-exclamation.svg
│     │  │     ├─ building-circle-xmark.svg
│     │  │     ├─ building-columns.svg
│     │  │     ├─ building-flag.svg
│     │  │     ├─ building-lock.svg
│     │  │     ├─ building-ngo.svg
│     │  │     ├─ building-shield.svg
│     │  │     ├─ building-un.svg
│     │  │     ├─ building-user.svg
│     │  │     ├─ building-wheat.svg
│     │  │     ├─ building.svg
│     │  │     ├─ bullhorn.svg
│     │  │     ├─ bullseye.svg
│     │  │     ├─ burger.svg
│     │  │     ├─ burst.svg
│     │  │     ├─ bus-simple.svg
│     │  │     ├─ bus.svg
│     │  │     ├─ business-time.svg
│     │  │     ├─ c.svg
│     │  │     ├─ cable-car.svg
│     │  │     ├─ cake-candles.svg
│     │  │     ├─ calculator.svg
│     │  │     ├─ calendar-check.svg
│     │  │     ├─ calendar-day.svg
│     │  │     ├─ calendar-days.svg
│     │  │     ├─ calendar-minus.svg
│     │  │     ├─ calendar-plus.svg
│     │  │     ├─ calendar-week.svg
│     │  │     ├─ calendar-xmark.svg
│     │  │     ├─ calendar.svg
│     │  │     ├─ camera-retro.svg
│     │  │     ├─ camera-rotate.svg
│     │  │     ├─ camera.svg
│     │  │     ├─ campground.svg
│     │  │     ├─ candy-cane.svg
│     │  │     ├─ cannabis.svg
│     │  │     ├─ capsules.svg
│     │  │     ├─ car-battery.svg
│     │  │     ├─ car-burst.svg
│     │  │     ├─ car-on.svg
│     │  │     ├─ car-rear.svg
│     │  │     ├─ car-side.svg
│     │  │     ├─ car-tunnel.svg
│     │  │     ├─ car.svg
│     │  │     ├─ caravan.svg
│     │  │     ├─ caret-down.svg
│     │  │     ├─ caret-left.svg
│     │  │     ├─ caret-right.svg
│     │  │     ├─ caret-up.svg
│     │  │     ├─ carrot.svg
│     │  │     ├─ cart-arrow-down.svg
│     │  │     ├─ cart-flatbed-suitcase.svg
│     │  │     ├─ cart-flatbed.svg
│     │  │     ├─ cart-plus.svg
│     │  │     ├─ cart-shopping.svg
│     │  │     ├─ cash-register.svg
│     │  │     ├─ cat.svg
│     │  │     ├─ cedi-sign.svg
│     │  │     ├─ cent-sign.svg
│     │  │     ├─ certificate.svg
│     │  │     ├─ chair.svg
│     │  │     ├─ chalkboard-user.svg
│     │  │     ├─ chalkboard.svg
│     │  │     ├─ champagne-glasses.svg
│     │  │     ├─ charging-station.svg
│     │  │     ├─ chart-area.svg
│     │  │     ├─ chart-bar.svg
│     │  │     ├─ chart-column.svg
│     │  │     ├─ chart-gantt.svg
│     │  │     ├─ chart-line.svg
│     │  │     ├─ chart-pie.svg
│     │  │     ├─ chart-simple.svg
│     │  │     ├─ check-double.svg
│     │  │     ├─ check-to-slot.svg
│     │  │     ├─ check.svg
│     │  │     ├─ cheese.svg
│     │  │     ├─ chess-bishop.svg
│     │  │     ├─ chess-board.svg
│     │  │     ├─ chess-king.svg
│     │  │     ├─ chess-knight.svg
│     │  │     ├─ chess-pawn.svg
│     │  │     ├─ chess-queen.svg
│     │  │     ├─ chess-rook.svg
│     │  │     ├─ chess.svg
│     │  │     ├─ chevron-down.svg
│     │  │     ├─ chevron-left.svg
│     │  │     ├─ chevron-right.svg
│     │  │     ├─ chevron-up.svg
│     │  │     ├─ child-combatant.svg
│     │  │     ├─ child-dress.svg
│     │  │     ├─ child-reaching.svg
│     │  │     ├─ child.svg
│     │  │     ├─ children.svg
│     │  │     ├─ church.svg
│     │  │     ├─ circle-arrow-down.svg
│     │  │     ├─ circle-arrow-left.svg
│     │  │     ├─ circle-arrow-right.svg
│     │  │     ├─ circle-arrow-up.svg
│     │  │     ├─ circle-check.svg
│     │  │     ├─ circle-chevron-down.svg
│     │  │     ├─ circle-chevron-left.svg
│     │  │     ├─ circle-chevron-right.svg
│     │  │     ├─ circle-chevron-up.svg
│     │  │     ├─ circle-dollar-to-slot.svg
│     │  │     ├─ circle-dot.svg
│     │  │     ├─ circle-down.svg
│     │  │     ├─ circle-exclamation.svg
│     │  │     ├─ circle-h.svg
│     │  │     ├─ circle-half-stroke.svg
│     │  │     ├─ circle-info.svg
│     │  │     ├─ circle-left.svg
│     │  │     ├─ circle-minus.svg
│     │  │     ├─ circle-nodes.svg
│     │  │     ├─ circle-notch.svg
│     │  │     ├─ circle-pause.svg
│     │  │     ├─ circle-play.svg
│     │  │     ├─ circle-plus.svg
│     │  │     ├─ circle-question.svg
│     │  │     ├─ circle-radiation.svg
│     │  │     ├─ circle-right.svg
│     │  │     ├─ circle-stop.svg
│     │  │     ├─ circle-up.svg
│     │  │     ├─ circle-user.svg
│     │  │     ├─ circle-xmark.svg
│     │  │     ├─ circle.svg
│     │  │     ├─ city.svg
│     │  │     ├─ clapperboard.svg
│     │  │     ├─ clipboard-check.svg
│     │  │     ├─ clipboard-list.svg
│     │  │     ├─ clipboard-question.svg
│     │  │     ├─ clipboard-user.svg
│     │  │     ├─ clipboard.svg
│     │  │     ├─ clock-rotate-left.svg
│     │  │     ├─ clock.svg
│     │  │     ├─ clone.svg
│     │  │     ├─ closed-captioning.svg
│     │  │     ├─ cloud-arrow-down.svg
│     │  │     ├─ cloud-arrow-up.svg
│     │  │     ├─ cloud-bolt.svg
│     │  │     ├─ cloud-meatball.svg
│     │  │     ├─ cloud-moon-rain.svg
│     │  │     ├─ cloud-moon.svg
│     │  │     ├─ cloud-rain.svg
│     │  │     ├─ cloud-showers-heavy.svg
│     │  │     ├─ cloud-showers-water.svg
│     │  │     ├─ cloud-sun-rain.svg
│     │  │     ├─ cloud-sun.svg
│     │  │     ├─ cloud.svg
│     │  │     ├─ clover.svg
│     │  │     ├─ code-branch.svg
│     │  │     ├─ code-commit.svg
│     │  │     ├─ code-compare.svg
│     │  │     ├─ code-fork.svg
│     │  │     ├─ code-merge.svg
│     │  │     ├─ code-pull-request.svg
│     │  │     ├─ code.svg
│     │  │     ├─ coins.svg
│     │  │     ├─ colon-sign.svg
│     │  │     ├─ comment-dollar.svg
│     │  │     ├─ comment-dots.svg
│     │  │     ├─ comment-medical.svg
│     │  │     ├─ comment-slash.svg
│     │  │     ├─ comment-sms.svg
│     │  │     ├─ comment.svg
│     │  │     ├─ comments-dollar.svg
│     │  │     ├─ comments.svg
│     │  │     ├─ compact-disc.svg
│     │  │     ├─ compass-drafting.svg
│     │  │     ├─ compass.svg
│     │  │     ├─ compress.svg
│     │  │     ├─ computer-mouse.svg
│     │  │     ├─ computer.svg
│     │  │     ├─ cookie-bite.svg
│     │  │     ├─ cookie.svg
│     │  │     ├─ copy.svg
│     │  │     ├─ copyright.svg
│     │  │     ├─ couch.svg
│     │  │     ├─ cow.svg
│     │  │     ├─ credit-card.svg
│     │  │     ├─ crop-simple.svg
│     │  │     ├─ crop.svg
│     │  │     ├─ cross.svg
│     │  │     ├─ crosshairs.svg
│     │  │     ├─ crow.svg
│     │  │     ├─ crown.svg
│     │  │     ├─ crutch.svg
│     │  │     ├─ cruzeiro-sign.svg
│     │  │     ├─ cube.svg
│     │  │     ├─ cubes-stacked.svg
│     │  │     ├─ cubes.svg
│     │  │     ├─ d.svg
│     │  │     ├─ database.svg
│     │  │     ├─ delete-left.svg
│     │  │     ├─ democrat.svg
│     │  │     ├─ desktop.svg
│     │  │     ├─ dharmachakra.svg
│     │  │     ├─ diagram-next.svg
│     │  │     ├─ diagram-predecessor.svg
│     │  │     ├─ diagram-project.svg
│     │  │     ├─ diagram-successor.svg
│     │  │     ├─ diamond-turn-right.svg
│     │  │     ├─ diamond.svg
│     │  │     ├─ dice-d20.svg
│     │  │     ├─ dice-d6.svg
│     │  │     ├─ dice-five.svg
│     │  │     ├─ dice-four.svg
│     │  │     ├─ dice-one.svg
│     │  │     ├─ dice-six.svg
│     │  │     ├─ dice-three.svg
│     │  │     ├─ dice-two.svg
│     │  │     ├─ dice.svg
│     │  │     ├─ disease.svg
│     │  │     ├─ display.svg
│     │  │     ├─ divide.svg
│     │  │     ├─ dna.svg
│     │  │     ├─ dog.svg
│     │  │     ├─ dollar-sign.svg
│     │  │     ├─ dolly.svg
│     │  │     ├─ dong-sign.svg
│     │  │     ├─ door-closed.svg
│     │  │     ├─ door-open.svg
│     │  │     ├─ dove.svg
│     │  │     ├─ down-left-and-up-right-to-center.svg
│     │  │     ├─ down-long.svg
│     │  │     ├─ download.svg
│     │  │     ├─ dragon.svg
│     │  │     ├─ draw-polygon.svg
│     │  │     ├─ droplet-slash.svg
│     │  │     ├─ droplet.svg
│     │  │     ├─ drum-steelpan.svg
│     │  │     ├─ drum.svg
│     │  │     ├─ drumstick-bite.svg
│     │  │     ├─ dumbbell.svg
│     │  │     ├─ dumpster-fire.svg
│     │  │     ├─ dumpster.svg
│     │  │     ├─ dungeon.svg
│     │  │     ├─ e.svg
│     │  │     ├─ ear-deaf.svg
│     │  │     ├─ ear-listen.svg
│     │  │     ├─ earth-africa.svg
│     │  │     ├─ earth-americas.svg
│     │  │     ├─ earth-asia.svg
│     │  │     ├─ earth-europe.svg
│     │  │     ├─ earth-oceania.svg
│     │  │     ├─ egg.svg
│     │  │     ├─ eject.svg
│     │  │     ├─ elevator.svg
│     │  │     ├─ ellipsis-vertical.svg
│     │  │     ├─ ellipsis.svg
│     │  │     ├─ envelope-circle-check.svg
│     │  │     ├─ envelope-open-text.svg
│     │  │     ├─ envelope-open.svg
│     │  │     ├─ envelope.svg
│     │  │     ├─ envelopes-bulk.svg
│     │  │     ├─ equals.svg
│     │  │     ├─ eraser.svg
│     │  │     ├─ ethernet.svg
│     │  │     ├─ euro-sign.svg
│     │  │     ├─ exclamation.svg
│     │  │     ├─ expand.svg
│     │  │     ├─ explosion.svg
│     │  │     ├─ eye-dropper.svg
│     │  │     ├─ eye-low-vision.svg
│     │  │     ├─ eye-slash.svg
│     │  │     ├─ eye.svg
│     │  │     ├─ f.svg
│     │  │     ├─ face-angry.svg
│     │  │     ├─ face-dizzy.svg
│     │  │     ├─ face-flushed.svg
│     │  │     ├─ face-frown-open.svg
│     │  │     ├─ face-frown.svg
│     │  │     ├─ face-grimace.svg
│     │  │     ├─ face-grin-beam-sweat.svg
│     │  │     ├─ face-grin-beam.svg
│     │  │     ├─ face-grin-hearts.svg
│     │  │     ├─ face-grin-squint-tears.svg
│     │  │     ├─ face-grin-squint.svg
│     │  │     ├─ face-grin-stars.svg
│     │  │     ├─ face-grin-tears.svg
│     │  │     ├─ face-grin-tongue-squint.svg
│     │  │     ├─ face-grin-tongue-wink.svg
│     │  │     ├─ face-grin-tongue.svg
│     │  │     ├─ face-grin-wide.svg
│     │  │     ├─ face-grin-wink.svg
│     │  │     ├─ face-grin.svg
│     │  │     ├─ face-kiss-beam.svg
│     │  │     ├─ face-kiss-wink-heart.svg
│     │  │     ├─ face-kiss.svg
│     │  │     ├─ face-laugh-beam.svg
│     │  │     ├─ face-laugh-squint.svg
│     │  │     ├─ face-laugh-wink.svg
│     │  │     ├─ face-laugh.svg
│     │  │     ├─ face-meh-blank.svg
│     │  │     ├─ face-meh.svg
│     │  │     ├─ face-rolling-eyes.svg
│     │  │     ├─ face-sad-cry.svg
│     │  │     ├─ face-sad-tear.svg
│     │  │     ├─ face-smile-beam.svg
│     │  │     ├─ face-smile-wink.svg
│     │  │     ├─ face-smile.svg
│     │  │     ├─ face-surprise.svg
│     │  │     ├─ face-tired.svg
│     │  │     ├─ fan.svg
│     │  │     ├─ faucet-drip.svg
│     │  │     ├─ faucet.svg
│     │  │     ├─ fax.svg
│     │  │     ├─ feather-pointed.svg
│     │  │     ├─ feather.svg
│     │  │     ├─ ferry.svg
│     │  │     ├─ file-arrow-down.svg
│     │  │     ├─ file-arrow-up.svg
│     │  │     ├─ file-audio.svg
│     │  │     ├─ file-circle-check.svg
│     │  │     ├─ file-circle-exclamation.svg
│     │  │     ├─ file-circle-minus.svg
│     │  │     ├─ file-circle-plus.svg
│     │  │     ├─ file-circle-question.svg
│     │  │     ├─ file-circle-xmark.svg
│     │  │     ├─ file-code.svg
│     │  │     ├─ file-contract.svg
│     │  │     ├─ file-csv.svg
│     │  │     ├─ file-excel.svg
│     │  │     ├─ file-export.svg
│     │  │     ├─ file-image.svg
│     │  │     ├─ file-import.svg
│     │  │     ├─ file-invoice-dollar.svg
│     │  │     ├─ file-invoice.svg
│     │  │     ├─ file-lines.svg
│     │  │     ├─ file-medical.svg
│     │  │     ├─ file-pdf.svg
│     │  │     ├─ file-pen.svg
│     │  │     ├─ file-powerpoint.svg
│     │  │     ├─ file-prescription.svg
│     │  │     ├─ file-shield.svg
│     │  │     ├─ file-signature.svg
│     │  │     ├─ file-video.svg
│     │  │     ├─ file-waveform.svg
│     │  │     ├─ file-word.svg
│     │  │     ├─ file-zipper.svg
│     │  │     ├─ file.svg
│     │  │     ├─ fill-drip.svg
│     │  │     ├─ fill.svg
│     │  │     ├─ film.svg
│     │  │     ├─ filter-circle-dollar.svg
│     │  │     ├─ filter-circle-xmark.svg
│     │  │     ├─ filter.svg
│     │  │     ├─ fingerprint.svg
│     │  │     ├─ fire-burner.svg
│     │  │     ├─ fire-extinguisher.svg
│     │  │     ├─ fire-flame-curved.svg
│     │  │     ├─ fire-flame-simple.svg
│     │  │     ├─ fire.svg
│     │  │     ├─ fish-fins.svg
│     │  │     ├─ fish.svg
│     │  │     ├─ flag-checkered.svg
│     │  │     ├─ flag-usa.svg
│     │  │     ├─ flag.svg
│     │  │     ├─ flask-vial.svg
│     │  │     ├─ flask.svg
│     │  │     ├─ floppy-disk.svg
│     │  │     ├─ florin-sign.svg
│     │  │     ├─ folder-closed.svg
│     │  │     ├─ folder-minus.svg
│     │  │     ├─ folder-open.svg
│     │  │     ├─ folder-plus.svg
│     │  │     ├─ folder-tree.svg
│     │  │     ├─ folder.svg
│     │  │     ├─ font-awesome.svg
│     │  │     ├─ font.svg
│     │  │     ├─ football.svg
│     │  │     ├─ forward-fast.svg
│     │  │     ├─ forward-step.svg
│     │  │     ├─ forward.svg
│     │  │     ├─ franc-sign.svg
│     │  │     ├─ frog.svg
│     │  │     ├─ futbol.svg
│     │  │     ├─ g.svg
│     │  │     ├─ gamepad.svg
│     │  │     ├─ gas-pump.svg
│     │  │     ├─ gauge-high.svg
│     │  │     ├─ gauge-simple-high.svg
│     │  │     ├─ gauge-simple.svg
│     │  │     ├─ gauge.svg
│     │  │     ├─ gavel.svg
│     │  │     ├─ gear.svg
│     │  │     ├─ gears.svg
│     │  │     ├─ gem.svg
│     │  │     ├─ genderless.svg
│     │  │     ├─ ghost.svg
│     │  │     ├─ gift.svg
│     │  │     ├─ gifts.svg
│     │  │     ├─ glass-water-droplet.svg
│     │  │     ├─ glass-water.svg
│     │  │     ├─ glasses.svg
│     │  │     ├─ globe.svg
│     │  │     ├─ golf-ball-tee.svg
│     │  │     ├─ gopuram.svg
│     │  │     ├─ graduation-cap.svg
│     │  │     ├─ greater-than-equal.svg
│     │  │     ├─ greater-than.svg
│     │  │     ├─ grip-lines-vertical.svg
│     │  │     ├─ grip-lines.svg
│     │  │     ├─ grip-vertical.svg
│     │  │     ├─ grip.svg
│     │  │     ├─ group-arrows-rotate.svg
│     │  │     ├─ guarani-sign.svg
│     │  │     ├─ guitar.svg
│     │  │     ├─ gun.svg
│     │  │     ├─ h.svg
│     │  │     ├─ hammer.svg
│     │  │     ├─ hamsa.svg
│     │  │     ├─ hand-back-fist.svg
│     │  │     ├─ hand-dots.svg
│     │  │     ├─ hand-fist.svg
│     │  │     ├─ hand-holding-dollar.svg
│     │  │     ├─ hand-holding-droplet.svg
│     │  │     ├─ hand-holding-hand.svg
│     │  │     ├─ hand-holding-heart.svg
│     │  │     ├─ hand-holding-medical.svg
│     │  │     ├─ hand-holding.svg
│     │  │     ├─ hand-lizard.svg
│     │  │     ├─ hand-middle-finger.svg
│     │  │     ├─ hand-peace.svg
│     │  │     ├─ hand-point-down.svg
│     │  │     ├─ hand-point-left.svg
│     │  │     ├─ hand-point-right.svg
│     │  │     ├─ hand-point-up.svg
│     │  │     ├─ hand-pointer.svg
│     │  │     ├─ hand-scissors.svg
│     │  │     ├─ hand-sparkles.svg
│     │  │     ├─ hand-spock.svg
│     │  │     ├─ hand.svg
│     │  │     ├─ handcuffs.svg
│     │  │     ├─ hands-asl-interpreting.svg
│     │  │     ├─ hands-bound.svg
│     │  │     ├─ hands-bubbles.svg
│     │  │     ├─ hands-clapping.svg
│     │  │     ├─ hands-holding-child.svg
│     │  │     ├─ hands-holding-circle.svg
│     │  │     ├─ hands-holding.svg
│     │  │     ├─ hands-praying.svg
│     │  │     ├─ hands.svg
│     │  │     ├─ handshake-angle.svg
│     │  │     ├─ handshake-simple-slash.svg
│     │  │     ├─ handshake-simple.svg
│     │  │     ├─ handshake-slash.svg
│     │  │     ├─ handshake.svg
│     │  │     ├─ hanukiah.svg
│     │  │     ├─ hard-drive.svg
│     │  │     ├─ hashtag.svg
│     │  │     ├─ hat-cowboy-side.svg
│     │  │     ├─ hat-cowboy.svg
│     │  │     ├─ hat-wizard.svg
│     │  │     ├─ head-side-cough-slash.svg
│     │  │     ├─ head-side-cough.svg
│     │  │     ├─ head-side-mask.svg
│     │  │     ├─ head-side-virus.svg
│     │  │     ├─ heading.svg
│     │  │     ├─ headphones-simple.svg
│     │  │     ├─ headphones.svg
│     │  │     ├─ headset.svg
│     │  │     ├─ heart-circle-bolt.svg
│     │  │     ├─ heart-circle-check.svg
│     │  │     ├─ heart-circle-exclamation.svg
│     │  │     ├─ heart-circle-minus.svg
│     │  │     ├─ heart-circle-plus.svg
│     │  │     ├─ heart-circle-xmark.svg
│     │  │     ├─ heart-crack.svg
│     │  │     ├─ heart-pulse.svg
│     │  │     ├─ heart.svg
│     │  │     ├─ helicopter-symbol.svg
│     │  │     ├─ helicopter.svg
│     │  │     ├─ helmet-safety.svg
│     │  │     ├─ helmet-un.svg
│     │  │     ├─ highlighter.svg
│     │  │     ├─ hill-avalanche.svg
│     │  │     ├─ hill-rockslide.svg
│     │  │     ├─ hippo.svg
│     │  │     ├─ hockey-puck.svg
│     │  │     ├─ holly-berry.svg
│     │  │     ├─ horse-head.svg
│     │  │     ├─ horse.svg
│     │  │     ├─ hospital-user.svg
│     │  │     ├─ hospital.svg
│     │  │     ├─ hot-tub-person.svg
│     │  │     ├─ hotdog.svg
│     │  │     ├─ hotel.svg
│     │  │     ├─ hourglass-end.svg
│     │  │     ├─ hourglass-half.svg
│     │  │     ├─ hourglass-start.svg
│     │  │     ├─ hourglass.svg
│     │  │     ├─ house-chimney-crack.svg
│     │  │     ├─ house-chimney-medical.svg
│     │  │     ├─ house-chimney-user.svg
│     │  │     ├─ house-chimney-window.svg
│     │  │     ├─ house-chimney.svg
│     │  │     ├─ house-circle-check.svg
│     │  │     ├─ house-circle-exclamation.svg
│     │  │     ├─ house-circle-xmark.svg
│     │  │     ├─ house-crack.svg
│     │  │     ├─ house-fire.svg
│     │  │     ├─ house-flag.svg
│     │  │     ├─ house-flood-water-circle-arrow-right.svg
│     │  │     ├─ house-flood-water.svg
│     │  │     ├─ house-laptop.svg
│     │  │     ├─ house-lock.svg
│     │  │     ├─ house-medical-circle-check.svg
│     │  │     ├─ house-medical-circle-exclamation.svg
│     │  │     ├─ house-medical-circle-xmark.svg
│     │  │     ├─ house-medical-flag.svg
│     │  │     ├─ house-medical.svg
│     │  │     ├─ house-signal.svg
│     │  │     ├─ house-tsunami.svg
│     │  │     ├─ house-user.svg
│     │  │     ├─ house.svg
│     │  │     ├─ hryvnia-sign.svg
│     │  │     ├─ hurricane.svg
│     │  │     ├─ i-cursor.svg
│     │  │     ├─ i.svg
│     │  │     ├─ ice-cream.svg
│     │  │     ├─ icicles.svg
│     │  │     ├─ icons.svg
│     │  │     ├─ id-badge.svg
│     │  │     ├─ id-card-clip.svg
│     │  │     ├─ id-card.svg
│     │  │     ├─ igloo.svg
│     │  │     ├─ image-portrait.svg
│     │  │     ├─ image.svg
│     │  │     ├─ images.svg
│     │  │     ├─ inbox.svg
│     │  │     ├─ indent.svg
│     │  │     ├─ indian-rupee-sign.svg
│     │  │     ├─ industry.svg
│     │  │     ├─ infinity.svg
│     │  │     ├─ info.svg
│     │  │     ├─ italic.svg
│     │  │     ├─ j.svg
│     │  │     ├─ jar-wheat.svg
│     │  │     ├─ jar.svg
│     │  │     ├─ jedi.svg
│     │  │     ├─ jet-fighter-up.svg
│     │  │     ├─ jet-fighter.svg
│     │  │     ├─ joint.svg
│     │  │     ├─ jug-detergent.svg
│     │  │     ├─ k.svg
│     │  │     ├─ kaaba.svg
│     │  │     ├─ key.svg
│     │  │     ├─ keyboard.svg
│     │  │     ├─ khanda.svg
│     │  │     ├─ kip-sign.svg
│     │  │     ├─ kit-medical.svg
│     │  │     ├─ kitchen-set.svg
│     │  │     ├─ kiwi-bird.svg
│     │  │     ├─ l.svg
│     │  │     ├─ land-mine-on.svg
│     │  │     ├─ landmark-dome.svg
│     │  │     ├─ landmark-flag.svg
│     │  │     ├─ landmark.svg
│     │  │     ├─ language.svg
│     │  │     ├─ laptop-code.svg
│     │  │     ├─ laptop-file.svg
│     │  │     ├─ laptop-medical.svg
│     │  │     ├─ laptop.svg
│     │  │     ├─ lari-sign.svg
│     │  │     ├─ layer-group.svg
│     │  │     ├─ leaf.svg
│     │  │     ├─ left-long.svg
│     │  │     ├─ left-right.svg
│     │  │     ├─ lemon.svg
│     │  │     ├─ less-than-equal.svg
│     │  │     ├─ less-than.svg
│     │  │     ├─ life-ring.svg
│     │  │     ├─ lightbulb.svg
│     │  │     ├─ lines-leaning.svg
│     │  │     ├─ link-slash.svg
│     │  │     ├─ link.svg
│     │  │     ├─ lira-sign.svg
│     │  │     ├─ list-check.svg
│     │  │     ├─ list-ol.svg
│     │  │     ├─ list-ul.svg
│     │  │     ├─ list.svg
│     │  │     ├─ litecoin-sign.svg
│     │  │     ├─ location-arrow.svg
│     │  │     ├─ location-crosshairs.svg
│     │  │     ├─ location-dot.svg
│     │  │     ├─ location-pin-lock.svg
│     │  │     ├─ location-pin.svg
│     │  │     ├─ lock-open.svg
│     │  │     ├─ lock.svg
│     │  │     ├─ locust.svg
│     │  │     ├─ lungs-virus.svg
│     │  │     ├─ lungs.svg
│     │  │     ├─ m.svg
│     │  │     ├─ magnet.svg
│     │  │     ├─ magnifying-glass-arrow-right.svg
│     │  │     ├─ magnifying-glass-chart.svg
│     │  │     ├─ magnifying-glass-dollar.svg
│     │  │     ├─ magnifying-glass-location.svg
│     │  │     ├─ magnifying-glass-minus.svg
│     │  │     ├─ magnifying-glass-plus.svg
│     │  │     ├─ magnifying-glass.svg
│     │  │     ├─ manat-sign.svg
│     │  │     ├─ map-location-dot.svg
│     │  │     ├─ map-location.svg
│     │  │     ├─ map-pin.svg
│     │  │     ├─ map.svg
│     │  │     ├─ marker.svg
│     │  │     ├─ mars-and-venus-burst.svg
│     │  │     ├─ mars-and-venus.svg
│     │  │     ├─ mars-double.svg
│     │  │     ├─ mars-stroke-right.svg
│     │  │     ├─ mars-stroke-up.svg
│     │  │     ├─ mars-stroke.svg
│     │  │     ├─ mars.svg
│     │  │     ├─ martini-glass-citrus.svg
│     │  │     ├─ martini-glass-empty.svg
│     │  │     ├─ martini-glass.svg
│     │  │     ├─ mask-face.svg
│     │  │     ├─ mask-ventilator.svg
│     │  │     ├─ mask.svg
│     │  │     ├─ masks-theater.svg
│     │  │     ├─ mattress-pillow.svg
│     │  │     ├─ maximize.svg
│     │  │     ├─ medal.svg
│     │  │     ├─ memory.svg
│     │  │     ├─ menorah.svg
│     │  │     ├─ mercury.svg
│     │  │     ├─ message.svg
│     │  │     ├─ meteor.svg
│     │  │     ├─ microchip.svg
│     │  │     ├─ microphone-lines-slash.svg
│     │  │     ├─ microphone-lines.svg
│     │  │     ├─ microphone-slash.svg
│     │  │     ├─ microphone.svg
│     │  │     ├─ microscope.svg
│     │  │     ├─ mill-sign.svg
│     │  │     ├─ minimize.svg
│     │  │     ├─ minus.svg
│     │  │     ├─ mitten.svg
│     │  │     ├─ mobile-button.svg
│     │  │     ├─ mobile-retro.svg
│     │  │     ├─ mobile-screen-button.svg
│     │  │     ├─ mobile-screen.svg
│     │  │     ├─ mobile.svg
│     │  │     ├─ money-bill-1-wave.svg
│     │  │     ├─ money-bill-1.svg
│     │  │     ├─ money-bill-transfer.svg
│     │  │     ├─ money-bill-trend-up.svg
│     │  │     ├─ money-bill-wave.svg
│     │  │     ├─ money-bill-wheat.svg
│     │  │     ├─ money-bill.svg
│     │  │     ├─ money-bills.svg
│     │  │     ├─ money-check-dollar.svg
│     │  │     ├─ money-check.svg
│     │  │     ├─ monument.svg
│     │  │     ├─ moon.svg
│     │  │     ├─ mortar-pestle.svg
│     │  │     ├─ mosque.svg
│     │  │     ├─ mosquito-net.svg
│     │  │     ├─ mosquito.svg
│     │  │     ├─ motorcycle.svg
│     │  │     ├─ mound.svg
│     │  │     ├─ mountain-city.svg
│     │  │     ├─ mountain-sun.svg
│     │  │     ├─ mountain.svg
│     │  │     ├─ mug-hot.svg
│     │  │     ├─ mug-saucer.svg
│     │  │     ├─ music.svg
│     │  │     ├─ n.svg
│     │  │     ├─ naira-sign.svg
│     │  │     ├─ network-wired.svg
│     │  │     ├─ neuter.svg
│     │  │     ├─ newspaper.svg
│     │  │     ├─ not-equal.svg
│     │  │     ├─ notdef.svg
│     │  │     ├─ note-sticky.svg
│     │  │     ├─ notes-medical.svg
│     │  │     ├─ o.svg
│     │  │     ├─ object-group.svg
│     │  │     ├─ object-ungroup.svg
│     │  │     ├─ oil-can.svg
│     │  │     ├─ oil-well.svg
│     │  │     ├─ om.svg
│     │  │     ├─ otter.svg
│     │  │     ├─ outdent.svg
│     │  │     ├─ p.svg
│     │  │     ├─ pager.svg
│     │  │     ├─ paint-roller.svg
│     │  │     ├─ paintbrush.svg
│     │  │     ├─ palette.svg
│     │  │     ├─ pallet.svg
│     │  │     ├─ panorama.svg
│     │  │     ├─ paper-plane.svg
│     │  │     ├─ paperclip.svg
│     │  │     ├─ parachute-box.svg
│     │  │     ├─ paragraph.svg
│     │  │     ├─ passport.svg
│     │  │     ├─ paste.svg
│     │  │     ├─ pause.svg
│     │  │     ├─ paw.svg
│     │  │     ├─ peace.svg
│     │  │     ├─ pen-clip.svg
│     │  │     ├─ pen-fancy.svg
│     │  │     ├─ pen-nib.svg
│     │  │     ├─ pen-ruler.svg
│     │  │     ├─ pen-to-square.svg
│     │  │     ├─ pen.svg
│     │  │     ├─ pencil.svg
│     │  │     ├─ people-arrows.svg
│     │  │     ├─ people-carry-box.svg
│     │  │     ├─ people-group.svg
│     │  │     ├─ people-line.svg
│     │  │     ├─ people-pulling.svg
│     │  │     ├─ people-robbery.svg
│     │  │     ├─ people-roof.svg
│     │  │     ├─ pepper-hot.svg
│     │  │     ├─ percent.svg
│     │  │     ├─ person-arrow-down-to-line.svg
│     │  │     ├─ person-arrow-up-from-line.svg
│     │  │     ├─ person-biking.svg
│     │  │     ├─ person-booth.svg
│     │  │     ├─ person-breastfeeding.svg
│     │  │     ├─ person-burst.svg
│     │  │     ├─ person-cane.svg
│     │  │     ├─ person-chalkboard.svg
│     │  │     ├─ person-circle-check.svg
│     │  │     ├─ person-circle-exclamation.svg
│     │  │     ├─ person-circle-minus.svg
│     │  │     ├─ person-circle-plus.svg
│     │  │     ├─ person-circle-question.svg
│     │  │     ├─ person-circle-xmark.svg
│     │  │     ├─ person-digging.svg
│     │  │     ├─ person-dots-from-line.svg
│     │  │     ├─ person-dress-burst.svg
│     │  │     ├─ person-dress.svg
│     │  │     ├─ person-drowning.svg
│     │  │     ├─ person-falling-burst.svg
│     │  │     ├─ person-falling.svg
│     │  │     ├─ person-half-dress.svg
│     │  │     ├─ person-harassing.svg
│     │  │     ├─ person-hiking.svg
│     │  │     ├─ person-military-pointing.svg
│     │  │     ├─ person-military-rifle.svg
│     │  │     ├─ person-military-to-person.svg
│     │  │     ├─ person-praying.svg
│     │  │     ├─ person-pregnant.svg
│     │  │     ├─ person-rays.svg
│     │  │     ├─ person-rifle.svg
│     │  │     ├─ person-running.svg
│     │  │     ├─ person-shelter.svg
│     │  │     ├─ person-skating.svg
│     │  │     ├─ person-skiing-nordic.svg
│     │  │     ├─ person-skiing.svg
│     │  │     ├─ person-snowboarding.svg
│     │  │     ├─ person-swimming.svg
│     │  │     ├─ person-through-window.svg
│     │  │     ├─ person-walking-arrow-loop-left.svg
│     │  │     ├─ person-walking-arrow-right.svg
│     │  │     ├─ person-walking-dashed-line-arrow-right.svg
│     │  │     ├─ person-walking-luggage.svg
│     │  │     ├─ person-walking-with-cane.svg
│     │  │     ├─ person-walking.svg
│     │  │     ├─ person.svg
│     │  │     ├─ peseta-sign.svg
│     │  │     ├─ peso-sign.svg
│     │  │     ├─ phone-flip.svg
│     │  │     ├─ phone-slash.svg
│     │  │     ├─ phone-volume.svg
│     │  │     ├─ phone.svg
│     │  │     ├─ photo-film.svg
│     │  │     ├─ piggy-bank.svg
│     │  │     ├─ pills.svg
│     │  │     ├─ pizza-slice.svg
│     │  │     ├─ place-of-worship.svg
│     │  │     ├─ plane-arrival.svg
│     │  │     ├─ plane-circle-check.svg
│     │  │     ├─ plane-circle-exclamation.svg
│     │  │     ├─ plane-circle-xmark.svg
│     │  │     ├─ plane-departure.svg
│     │  │     ├─ plane-lock.svg
│     │  │     ├─ plane-slash.svg
│     │  │     ├─ plane-up.svg
│     │  │     ├─ plane.svg
│     │  │     ├─ plant-wilt.svg
│     │  │     ├─ plate-wheat.svg
│     │  │     ├─ play.svg
│     │  │     ├─ plug-circle-bolt.svg
│     │  │     ├─ plug-circle-check.svg
│     │  │     ├─ plug-circle-exclamation.svg
│     │  │     ├─ plug-circle-minus.svg
│     │  │     ├─ plug-circle-plus.svg
│     │  │     ├─ plug-circle-xmark.svg
│     │  │     ├─ plug.svg
│     │  │     ├─ plus-minus.svg
│     │  │     ├─ plus.svg
│     │  │     ├─ podcast.svg
│     │  │     ├─ poo-storm.svg
│     │  │     ├─ poo.svg
│     │  │     ├─ poop.svg
│     │  │     ├─ power-off.svg
│     │  │     ├─ prescription-bottle-medical.svg
│     │  │     ├─ prescription-bottle.svg
│     │  │     ├─ prescription.svg
│     │  │     ├─ print.svg
│     │  │     ├─ pump-medical.svg
│     │  │     ├─ pump-soap.svg
│     │  │     ├─ puzzle-piece.svg
│     │  │     ├─ q.svg
│     │  │     ├─ qrcode.svg
│     │  │     ├─ question.svg
│     │  │     ├─ quote-left.svg
│     │  │     ├─ quote-right.svg
│     │  │     ├─ r.svg
│     │  │     ├─ radiation.svg
│     │  │     ├─ radio.svg
│     │  │     ├─ rainbow.svg
│     │  │     ├─ ranking-star.svg
│     │  │     ├─ receipt.svg
│     │  │     ├─ record-vinyl.svg
│     │  │     ├─ rectangle-ad.svg
│     │  │     ├─ rectangle-list.svg
│     │  │     ├─ rectangle-xmark.svg
│     │  │     ├─ recycle.svg
│     │  │     ├─ registered.svg
│     │  │     ├─ repeat.svg
│     │  │     ├─ reply-all.svg
│     │  │     ├─ reply.svg
│     │  │     ├─ republican.svg
│     │  │     ├─ restroom.svg
│     │  │     ├─ retweet.svg
│     │  │     ├─ ribbon.svg
│     │  │     ├─ right-from-bracket.svg
│     │  │     ├─ right-left.svg
│     │  │     ├─ right-long.svg
│     │  │     ├─ right-to-bracket.svg
│     │  │     ├─ ring.svg
│     │  │     ├─ road-barrier.svg
│     │  │     ├─ road-bridge.svg
│     │  │     ├─ road-circle-check.svg
│     │  │     ├─ road-circle-exclamation.svg
│     │  │     ├─ road-circle-xmark.svg
│     │  │     ├─ road-lock.svg
│     │  │     ├─ road-spikes.svg
│     │  │     ├─ road.svg
│     │  │     ├─ robot.svg
│     │  │     ├─ rocket.svg
│     │  │     ├─ rotate-left.svg
│     │  │     ├─ rotate-right.svg
│     │  │     ├─ rotate.svg
│     │  │     ├─ route.svg
│     │  │     ├─ rss.svg
│     │  │     ├─ ruble-sign.svg
│     │  │     ├─ rug.svg
│     │  │     ├─ ruler-combined.svg
│     │  │     ├─ ruler-horizontal.svg
│     │  │     ├─ ruler-vertical.svg
│     │  │     ├─ ruler.svg
│     │  │     ├─ rupee-sign.svg
│     │  │     ├─ rupiah-sign.svg
│     │  │     ├─ s.svg
│     │  │     ├─ sack-dollar.svg
│     │  │     ├─ sack-xmark.svg
│     │  │     ├─ sailboat.svg
│     │  │     ├─ satellite-dish.svg
│     │  │     ├─ satellite.svg
│     │  │     ├─ scale-balanced.svg
│     │  │     ├─ scale-unbalanced-flip.svg
│     │  │     ├─ scale-unbalanced.svg
│     │  │     ├─ school-circle-check.svg
│     │  │     ├─ school-circle-exclamation.svg
│     │  │     ├─ school-circle-xmark.svg
│     │  │     ├─ school-flag.svg
│     │  │     ├─ school-lock.svg
│     │  │     ├─ school.svg
│     │  │     ├─ scissors.svg
│     │  │     ├─ screwdriver-wrench.svg
│     │  │     ├─ screwdriver.svg
│     │  │     ├─ scroll-torah.svg
│     │  │     ├─ scroll.svg
│     │  │     ├─ sd-card.svg
│     │  │     ├─ section.svg
│     │  │     ├─ seedling.svg
│     │  │     ├─ server.svg
│     │  │     ├─ shapes.svg
│     │  │     ├─ share-from-square.svg
│     │  │     ├─ share-nodes.svg
│     │  │     ├─ share.svg
│     │  │     ├─ sheet-plastic.svg
│     │  │     ├─ shekel-sign.svg
│     │  │     ├─ shield-cat.svg
│     │  │     ├─ shield-dog.svg
│     │  │     ├─ shield-halved.svg
│     │  │     ├─ shield-heart.svg
│     │  │     ├─ shield-virus.svg
│     │  │     ├─ shield.svg
│     │  │     ├─ ship.svg
│     │  │     ├─ shirt.svg
│     │  │     ├─ shoe-prints.svg
│     │  │     ├─ shop-lock.svg
│     │  │     ├─ shop-slash.svg
│     │  │     ├─ shop.svg
│     │  │     ├─ shower.svg
│     │  │     ├─ shrimp.svg
│     │  │     ├─ shuffle.svg
│     │  │     ├─ shuttle-space.svg
│     │  │     ├─ sign-hanging.svg
│     │  │     ├─ signal.svg
│     │  │     ├─ signature.svg
│     │  │     ├─ signs-post.svg
│     │  │     ├─ sim-card.svg
│     │  │     ├─ sink.svg
│     │  │     ├─ skull-crossbones.svg
│     │  │     ├─ skull.svg
│     │  │     ├─ slash.svg
│     │  │     ├─ sleigh.svg
│     │  │     ├─ sliders.svg
│     │  │     ├─ smog.svg
│     │  │     ├─ smoking.svg
│     │  │     ├─ snowflake.svg
│     │  │     ├─ snowman.svg
│     │  │     ├─ snowplow.svg
│     │  │     ├─ soap.svg
│     │  │     ├─ socks.svg
│     │  │     ├─ solar-panel.svg
│     │  │     ├─ sort-down.svg
│     │  │     ├─ sort-up.svg
│     │  │     ├─ sort.svg
│     │  │     ├─ spa.svg
│     │  │     ├─ spaghetti-monster-flying.svg
│     │  │     ├─ spell-check.svg
│     │  │     ├─ spider.svg
│     │  │     ├─ spinner.svg
│     │  │     ├─ splotch.svg
│     │  │     ├─ spoon.svg
│     │  │     ├─ spray-can-sparkles.svg
│     │  │     ├─ spray-can.svg
│     │  │     ├─ square-arrow-up-right.svg
│     │  │     ├─ square-caret-down.svg
│     │  │     ├─ square-caret-left.svg
│     │  │     ├─ square-caret-right.svg
│     │  │     ├─ square-caret-up.svg
│     │  │     ├─ square-check.svg
│     │  │     ├─ square-envelope.svg
│     │  │     ├─ square-full.svg
│     │  │     ├─ square-h.svg
│     │  │     ├─ square-minus.svg
│     │  │     ├─ square-nfi.svg
│     │  │     ├─ square-parking.svg
│     │  │     ├─ square-pen.svg
│     │  │     ├─ square-person-confined.svg
│     │  │     ├─ square-phone-flip.svg
│     │  │     ├─ square-phone.svg
│     │  │     ├─ square-plus.svg
│     │  │     ├─ square-poll-horizontal.svg
│     │  │     ├─ square-poll-vertical.svg
│     │  │     ├─ square-root-variable.svg
│     │  │     ├─ square-rss.svg
│     │  │     ├─ square-share-nodes.svg
│     │  │     ├─ square-up-right.svg
│     │  │     ├─ square-virus.svg
│     │  │     ├─ square-xmark.svg
│     │  │     ├─ square.svg
│     │  │     ├─ staff-snake.svg
│     │  │     ├─ stairs.svg
│     │  │     ├─ stamp.svg
│     │  │     ├─ stapler.svg
│     │  │     ├─ star-and-crescent.svg
│     │  │     ├─ star-half-stroke.svg
│     │  │     ├─ star-half.svg
│     │  │     ├─ star-of-david.svg
│     │  │     ├─ star-of-life.svg
│     │  │     ├─ star.svg
│     │  │     ├─ sterling-sign.svg
│     │  │     ├─ stethoscope.svg
│     │  │     ├─ stop.svg
│     │  │     ├─ stopwatch-20.svg
│     │  │     ├─ stopwatch.svg
│     │  │     ├─ store-slash.svg
│     │  │     ├─ store.svg
│     │  │     ├─ street-view.svg
│     │  │     ├─ strikethrough.svg
│     │  │     ├─ stroopwafel.svg
│     │  │     ├─ subscript.svg
│     │  │     ├─ suitcase-medical.svg
│     │  │     ├─ suitcase-rolling.svg
│     │  │     ├─ suitcase.svg
│     │  │     ├─ sun-plant-wilt.svg
│     │  │     ├─ sun.svg
│     │  │     ├─ superscript.svg
│     │  │     ├─ swatchbook.svg
│     │  │     ├─ synagogue.svg
│     │  │     ├─ syringe.svg
│     │  │     ├─ t.svg
│     │  │     ├─ table-cells-large.svg
│     │  │     ├─ table-cells.svg
│     │  │     ├─ table-columns.svg
│     │  │     ├─ table-list.svg
│     │  │     ├─ table-tennis-paddle-ball.svg
│     │  │     ├─ table.svg
│     │  │     ├─ tablet-button.svg
│     │  │     ├─ tablet-screen-button.svg
│     │  │     ├─ tablet.svg
│     │  │     ├─ tablets.svg
│     │  │     ├─ tachograph-digital.svg
│     │  │     ├─ tag.svg
│     │  │     ├─ tags.svg
│     │  │     ├─ tape.svg
│     │  │     ├─ tarp-droplet.svg
│     │  │     ├─ tarp.svg
│     │  │     ├─ taxi.svg
│     │  │     ├─ teeth-open.svg
│     │  │     ├─ teeth.svg
│     │  │     ├─ temperature-arrow-down.svg
│     │  │     ├─ temperature-arrow-up.svg
│     │  │     ├─ temperature-empty.svg
│     │  │     ├─ temperature-full.svg
│     │  │     ├─ temperature-half.svg
│     │  │     ├─ temperature-high.svg
│     │  │     ├─ temperature-low.svg
│     │  │     ├─ temperature-quarter.svg
│     │  │     ├─ temperature-three-quarters.svg
│     │  │     ├─ tenge-sign.svg
│     │  │     ├─ tent-arrow-down-to-line.svg
│     │  │     ├─ tent-arrow-left-right.svg
│     │  │     ├─ tent-arrow-turn-left.svg
│     │  │     ├─ tent-arrows-down.svg
│     │  │     ├─ tent.svg
│     │  │     ├─ tents.svg
│     │  │     ├─ terminal.svg
│     │  │     ├─ text-height.svg
│     │  │     ├─ text-slash.svg
│     │  │     ├─ text-width.svg
│     │  │     ├─ thermometer.svg
│     │  │     ├─ thumbs-down.svg
│     │  │     ├─ thumbs-up.svg
│     │  │     ├─ thumbtack.svg
│     │  │     ├─ ticket-simple.svg
│     │  │     ├─ ticket.svg
│     │  │     ├─ timeline.svg
│     │  │     ├─ toggle-off.svg
│     │  │     ├─ toggle-on.svg
│     │  │     ├─ toilet-paper-slash.svg
│     │  │     ├─ toilet-paper.svg
│     │  │     ├─ toilet-portable.svg
│     │  │     ├─ toilet.svg
│     │  │     ├─ toilets-portable.svg
│     │  │     ├─ toolbox.svg
│     │  │     ├─ tooth.svg
│     │  │     ├─ torii-gate.svg
│     │  │     ├─ tornado.svg
│     │  │     ├─ tower-broadcast.svg
│     │  │     ├─ tower-cell.svg
│     │  │     ├─ tower-observation.svg
│     │  │     ├─ tractor.svg
│     │  │     ├─ trademark.svg
│     │  │     ├─ traffic-light.svg
│     │  │     ├─ trailer.svg
│     │  │     ├─ train-subway.svg
│     │  │     ├─ train-tram.svg
│     │  │     ├─ train.svg
│     │  │     ├─ transgender.svg
│     │  │     ├─ trash-arrow-up.svg
│     │  │     ├─ trash-can-arrow-up.svg
│     │  │     ├─ trash-can.svg
│     │  │     ├─ trash.svg
│     │  │     ├─ tree-city.svg
│     │  │     ├─ tree.svg
│     │  │     ├─ triangle-exclamation.svg
│     │  │     ├─ trophy.svg
│     │  │     ├─ trowel-bricks.svg
│     │  │     ├─ trowel.svg
│     │  │     ├─ truck-arrow-right.svg
│     │  │     ├─ truck-droplet.svg
│     │  │     ├─ truck-fast.svg
│     │  │     ├─ truck-field-un.svg
│     │  │     ├─ truck-field.svg
│     │  │     ├─ truck-front.svg
│     │  │     ├─ truck-medical.svg
│     │  │     ├─ truck-monster.svg
│     │  │     ├─ truck-moving.svg
│     │  │     ├─ truck-pickup.svg
│     │  │     ├─ truck-plane.svg
│     │  │     ├─ truck-ramp-box.svg
│     │  │     ├─ truck.svg
│     │  │     ├─ tty.svg
│     │  │     ├─ turkish-lira-sign.svg
│     │  │     ├─ turn-down.svg
│     │  │     ├─ turn-up.svg
│     │  │     ├─ tv.svg
│     │  │     ├─ u.svg
│     │  │     ├─ umbrella-beach.svg
│     │  │     ├─ umbrella.svg
│     │  │     ├─ underline.svg
│     │  │     ├─ universal-access.svg
│     │  │     ├─ unlock-keyhole.svg
│     │  │     ├─ unlock.svg
│     │  │     ├─ up-down-left-right.svg
│     │  │     ├─ up-down.svg
│     │  │     ├─ up-long.svg
│     │  │     ├─ up-right-and-down-left-from-center.svg
│     │  │     ├─ up-right-from-square.svg
│     │  │     ├─ upload.svg
│     │  │     ├─ user-astronaut.svg
│     │  │     ├─ user-check.svg
│     │  │     ├─ user-clock.svg
│     │  │     ├─ user-doctor.svg
│     │  │     ├─ user-gear.svg
│     │  │     ├─ user-graduate.svg
│     │  │     ├─ user-group.svg
│     │  │     ├─ user-injured.svg
│     │  │     ├─ user-large-slash.svg
│     │  │     ├─ user-large.svg
│     │  │     ├─ user-lock.svg
│     │  │     ├─ user-minus.svg
│     │  │     ├─ user-ninja.svg
│     │  │     ├─ user-nurse.svg
│     │  │     ├─ user-pen.svg
│     │  │     ├─ user-plus.svg
│     │  │     ├─ user-secret.svg
│     │  │     ├─ user-shield.svg
│     │  │     ├─ user-slash.svg
│     │  │     ├─ user-tag.svg
│     │  │     ├─ user-tie.svg
│     │  │     ├─ user-xmark.svg
│     │  │     ├─ user.svg
│     │  │     ├─ users-between-lines.svg
│     │  │     ├─ users-gear.svg
│     │  │     ├─ users-line.svg
│     │  │     ├─ users-rays.svg
│     │  │     ├─ users-rectangle.svg
│     │  │     ├─ users-slash.svg
│     │  │     ├─ users-viewfinder.svg
│     │  │     ├─ users.svg
│     │  │     ├─ utensils.svg
│     │  │     ├─ v.svg
│     │  │     ├─ van-shuttle.svg
│     │  │     ├─ vault.svg
│     │  │     ├─ vector-square.svg
│     │  │     ├─ venus-double.svg
│     │  │     ├─ venus-mars.svg
│     │  │     ├─ venus.svg
│     │  │     ├─ vest-patches.svg
│     │  │     ├─ vest.svg
│     │  │     ├─ vial-circle-check.svg
│     │  │     ├─ vial-virus.svg
│     │  │     ├─ vial.svg
│     │  │     ├─ vials.svg
│     │  │     ├─ video-slash.svg
│     │  │     ├─ video.svg
│     │  │     ├─ vihara.svg
│     │  │     ├─ virus-covid-slash.svg
│     │  │     ├─ virus-covid.svg
│     │  │     ├─ virus-slash.svg
│     │  │     ├─ virus.svg
│     │  │     ├─ viruses.svg
│     │  │     ├─ voicemail.svg
│     │  │     ├─ volcano.svg
│     │  │     ├─ volleyball.svg
│     │  │     ├─ volume-high.svg
│     │  │     ├─ volume-low.svg
│     │  │     ├─ volume-off.svg
│     │  │     ├─ volume-xmark.svg
│     │  │     ├─ vr-cardboard.svg
│     │  │     ├─ w.svg
│     │  │     ├─ walkie-talkie.svg
│     │  │     ├─ wallet.svg
│     │  │     ├─ wand-magic-sparkles.svg
│     │  │     ├─ wand-magic.svg
│     │  │     ├─ wand-sparkles.svg
│     │  │     ├─ warehouse.svg
│     │  │     ├─ water-ladder.svg
│     │  │     ├─ water.svg
│     │  │     ├─ wave-square.svg
│     │  │     ├─ weight-hanging.svg
│     │  │     ├─ weight-scale.svg
│     │  │     ├─ wheat-awn-circle-exclamation.svg
│     │  │     ├─ wheat-awn.svg
│     │  │     ├─ wheelchair-move.svg
│     │  │     ├─ wheelchair.svg
│     │  │     ├─ whiskey-glass.svg
│     │  │     ├─ wifi.svg
│     │  │     ├─ wind.svg
│     │  │     ├─ window-maximize.svg
│     │  │     ├─ window-minimize.svg
│     │  │     ├─ window-restore.svg
│     │  │     ├─ wine-bottle.svg
│     │  │     ├─ wine-glass-empty.svg
│     │  │     ├─ wine-glass.svg
│     │  │     ├─ won-sign.svg
│     │  │     ├─ worm.svg
│     │  │     ├─ wrench.svg
│     │  │     ├─ x-ray.svg
│     │  │     ├─ x.svg
│     │  │     ├─ xmark.svg
│     │  │     ├─ xmarks-lines.svg
│     │  │     ├─ y.svg
│     │  │     ├─ yen-sign.svg
│     │  │     ├─ yin-yang.svg
│     │  │     └─ z.svg
│     │  └─ webfonts
│     │     ├─ fa-brands-400.ttf
│     │     ├─ fa-brands-400.woff2
│     │     ├─ fa-regular-400.ttf
│     │     ├─ fa-regular-400.woff2
│     │     ├─ fa-solid-900.ttf
│     │     ├─ fa-solid-900.woff2
│     │     ├─ fa-v4compatibility.ttf
│     │     └─ fa-v4compatibility.woff2
│     └─ jquery-3.7.1
│        └─ jquery-3.7.1.min.js
└─ templates
   ├─ 400.html
   ├─ 403.html
   ├─ 404.html
   ├─ 500.html
   ├─ accounts
   │  ├─ add_staff.html
   │  ├─ add_student.html
   │  ├─ edit_lecturer.html
   │  ├─ edit_student.html
   │  ├─ lecturer_list.html
   │  ├─ parent_form.html
   │  ├─ profile.html
   │  ├─ profile_single.html
   │  └─ student_list.html
   ├─ aside.html
   ├─ base.html
   ├─ chatbot.html
   ├─ core
   │  ├─ dashboard.html
   │  ├─ index.html
   │  ├─ post_add.html
   │  ├─ semester_list.html
   │  ├─ semester_update.html
   │  ├─ session_list.html
   │  └─ session_update.html
   ├─ correct_answer.html
   ├─ course
   │  ├─ course_add.html
   │  ├─ course_allocation_form.html
   │  ├─ course_allocation_view.html
   │  ├─ course_registration.html
   │  ├─ course_single.html
   │  ├─ program_add.html
   │  ├─ program_list.html
   │  ├─ program_single.html
   │  └─ user_course_list.html
   ├─ error_handler_base.html
   ├─ index.html
   ├─ invoices.html
   ├─ invoice_detail.html
   ├─ navbar.html
   ├─ pdf
   │  ├─ lecturer_list.html
   │  ├─ profile_single.html
   │  └─ student_list.html
   ├─ privacy.html
   ├─ progress.html
   ├─ question.html
   ├─ registration
   │  ├─ login.html
   │  ├─ password_reset.html
   │  ├─ password_reset_complete.html
   │  ├─ password_reset_confirm.html
   │  ├─ password_reset_done.html
   │  ├─ register.html
   │  └─ registration_base.html
   ├─ result.html
   ├─ search
   │  └─ search_view.html
   ├─ setting
   │  ├─ admin_panel.html
   │  ├─ password_change.html
   │  └─ profile_info_change.html
   ├─ snippets
   │  ├─ filter_form.html
   │  └─ messages.html
   ├─ term.html
   └─ upload
      ├─ upload_file_form.html
      ├─ upload_video_form.html
      └─ video_single.html

```