#region Text
#region Menu
menu_title = ["بخش مورد نظر خود را انتخاب کنید", "Select your desired section"]
menu_guide = ["1. راهنما", "1. Guide"]
menu_setting = ["2. تنظیمات", "2. Setting"]
menu_read = ["3. خواندن جوک", "3. Read joke"]
menu_add = ["4. اضافه کردن جوک", "4. Add joke"]
menu_del = ["5. حذف جوک", "5. Delete joke"]
menu_export = ["6. استخراج جوک", "6. Extract joke"]

def menu_about(num):
    return [f"{num}. درباره ما", f"{num}. About us"]

def menu_exit(num):
    return [f"{num}. خروج از برنامه", f"{num}. Exit program"]
#endregion Menu
#region Inputs
input_guide = ["1. دریافت ایمیل پشتیبانی\n2. منو برنامه\n3. خروج از برنامه\n", "1. Receive email support\n2. Program menu\n3. Exit program"]
input_log_on = ["در حال حاضر گزارش برای شما فعال میباشد\n\n1. غیرفعال کردن گزارش\n2. بازگشت به منو برنامه", "Currently, logging is enabled for you.\n1. Disable logging\n2. Return to program menu"]
input_account = ["لطفا نوع اشتراک خود را انتخاب کنید\n1. ورود\n2. ثبت نام\n3. مهمان", "Please select your subscription type\n1. Login\n2. Sign up\n3. Guest"]
input_log_off = ["در حال حاضر گزارش برای شما غیرفعال میباشد.\n\n1. فعال کردن گزارش \n2. بازگشت به منو برنامه", "Currently, logging is disabled for you.\n1. Enable logging\n2. Return to program menu"]
input_password = ["کد دسترسی را وارد کنید", "Enter the access code"]
input_jock_num = ["چه تعداد جوک میخواهید؟", "How many jokes do you want?"]
input_your_joke = ["جوک خود را وارد کنید", "Enter your joke"]
input_mini_menu = ["1. منو برنامه\n2. خروج از برنامه\n", "1. Program menu\n2. Exit program"]
input_setting_menu = ["تنظیمات مورد نظر خود را انتخاب کنید\n\n1. تنظیم زبان\n2. تنظیمات لاگ\n3. بازگشت به منو برنامه", "Select your desired settings\n\n1. Language settings\n2. Log settings\n3. Return to program menu"]
input_jock_exporter = ["بخش مورد نظر خود را انتخاب کنید\n\n1. استخراج جوک به تعداد دلخواه\n2. استخراج تمام جوک ها\n3. یازگشت به منو برنامه", "Select your desired section\n\n1. Extract jokes by quantity\n2. Extract all jokes\n3. Return to program menu"]
input_select_language = ["1. فارسی\n2. English", "1. فارسی\n2. English"]  # Fa
input_jock_deleter_m1 = ["متن جوک مورد نظر خود را کامل و با جزئیات وارد کنید", "Enter the complete and detailed text of the joke you want"]
input_jock_deleter_m2 = ["عدد جوک مورد نظر خود را وارد کنید", "Enter the number of the joke you want"]
input_select_user_type = ["لطفا نوع کاربری خود را انتخاب کنید\n1. کاربر\n2. نویسنده\n3. مدیر", "Please select your user type\n1. User\n2. Author\n3. Admin"]
input_jock_reader_menu = ["بخش مورد نظر خود را انتخاب کنید\n\n1. نمایش 1 جوک\n2. نمایش جوک به تعداد دلخواه\n3. نمایش تمام جوک ها\n4. یازگشت به منو برنامه", "Select your desired section\n\n1. Show 1 joke\n2. Show jokes by quantity\n3. Show all jokes\n4. Return to program menu"]
input_jock_deleter_menu = ["بخش مورد نظر خود را انتخاب کنید\n\n حذف خود را انتخاب کنید\n1. حذف با متن\n2. حذف با شماره \n3. حذف شانسی\n4. یازگشت به منو برنامه", "Select your desired section\n\nSelect your deletion method\n1. Delete by text\n2. Delete by number\n3. Random deletion\n4. Return to program menu"]

input_username = ["نام کاربری خود را وارد کنید", "Enter your username:"]
input_password = ["رمز خود را وارد کنید", "Enter your password:"]

#endregion Inputs
#region Prints
print_email_support = ["پشتیبانی: report.riazmand@gmail.com\n", "Support: report.riazmand@gmail.com\n"]
print_about = ["مشخصات سازنده\nنام و نام خانوادگی: آرمین دوست محمدی\nپایه و رشته تحصیلی: پایه دهم، رشته ریاضی فیزیک\n", "Developer Information\nFull name: Armin Dost Mohammadi\nGrade and Field of Study: 10th Grade, Math-Physics\n"]
print_guide = ["این برنامه به گونه ای طراحی شده است که کاربر پسند باشد و به راهنمای خاصی نیاز ندارد. با این حال، اگر به کمک نیاز دارید، لطفاً در تماس با تیم پشتیبانی ما تردید نکنید\n", "This program is designed to be user-friendly and does not require a special guide. However, if you need any assistance, please don't hesitate to reach out to our support team.\n"]
print_email = ["در حال ارسال ایمیل به پشتیبانی، لطفا صبر کنید", "Sending email to support, please wait"]
print_crash = ["برنامه مشکل پیدا کرد! برنامه در حال حاضر با یک خطا مواجه است\nدر حال ارسال ایمیل به پشتیبانی، لطفا صبر کنید", "Program was crashed! The program is currently experiencing an error\nSending email to support, please wait"]
print_welcome = ["سلام کاربر عزیز. به برنامه 'ریاضمند' خوش آمدید\n", "Hi dear user. Welcome to the 'Riazmand' program\n"]
print_save_user = ["ثبت نام با موفقیت انجام شد", "Registration was successful!"]
print_exit_true = ["ایمیل ارسال شد\nبرنامه بسته شد", "Email was sent\nProgram closed."]
print_exit_false = ["ایمیل ارسال نشد\nبرنامه بسته شد", "Email wasn't sent\nProgram closed."]
print_jock_added = ["جوک شما افزوده شد", "Your joke has been added"]
print_login_error = ["نام کاربری یا رمز عبور اشتباه است. لطفا دوباره تلاش کنید", "Invalid username or password. Please try again."]
print_value_erorr = ["خطا! ورودی نامعتبر است", "Error! Invalid input"]
print_jock_deleted = ["جوک مورد نظر پاک شد", "The joke has been deleted"]
print_pass_len_error = ["طول پسورد باید حداقل 8 کاراکتر باشد", "Password should be at least 8 characters long!"]
print_password_erorr = ["خطا! رمز عبور اشتباه است. دوباره تلاش کنید", "Error! The password is incorrect. Try again."]
print_username_exists = ["نام کاربری مورد نظر قبلا انتخاب شده است", "Username already exists!"]
print_select_language = ["لطفا زبان خود را انتخاب کنید\n", "Please select your language\n"]  # Fa
print_user_access_root = ["کد مخفی تایید شد! دسترسی ریشه (بالاترین سطح دسترسی) فعال شد", "Secret code confirmed! Root access (highest level of access) activated"]
print_user_access_user = ["دسترسی کاربر فعال شد", "User access activated"]
print_user_access_admin = ["دسترسی مدیر فعال شد", "Admin access activated"]
print_user_access_auther = ["دسترسی نویسنده فعال شد", "Author access activated"]
print_random_jock_deleted = ["یک جوک به صورت شانسی حذف شد", "A joke has been randomly deleted"]
print_select_language_erorr = ["\nورودی نامعتبر! به طور پیش فرض زبان فارسی انتخاب شد", "\nInvalid input! Persian language selected by default"]  # Fa
print_select_user_type_erorr = ["\nورودی نامعتبر! به طور پیش فرض 'کاربر' انتخاب شد", "\nInvalid input! 'User' selected by default"]

def print_file_saved(fname):
    return [f"\nجوک ها ذخیره شدند\nC:\\Riazmand/Exports/{fname}", f"\nJocks are saved\nC:\\Riazmand/Exports/{fname}"]
#endregion Prints
#region Logs
log_exit = ["در حال بستن برنامه توسط کاربر\nدر حال ارسال ایمیل به پشتیبانی، لطفا صبر کنید", "The program is being closed by the user\nSending email to support, please wait"]
log_start = ["برنامه شروع به کارکرد", "Program started"]
log_erorr = ["خطایی توسط کاربر رخ داد، در حال پرداز و اعلام خطا به کاربر", "Error occurred, processing and reporting to user"]
log_language = ["زبان برنامه انتخاب شد", "Language selected"]
log_select_user_type = ["نوع کاربر انتخاب شد. در انتظار تایید دسترسی", "User type selected, waiting for access confirmation"]
log_user_access_confirmrd = ["دسترسی کاربر تایید و فعال شد", "User access confirmed and activated"]
log_user_access_show = ["سطح دسترسی به کاربر اعلام شد", "Access level announced to user"]
log_menu = ["منو برنامه باز شد", "Menu opened"]
log_get_jocks = ["پردازش بر روی جوک ها انجام شد", "Jokes processed"]
log_1_jock_showed = ["یک جوک به کاربر نمایش داده شد", "One joke shown to user"]
log_some_jocks_showed = ["مقداری جوک به کاربر نمایش داده شد", "Some jokes shown to user"]
log_all_jocks_showed = ["تمام جوک ها به کاربر نمایش داده شد", "All jokes shown to user"]
log_1_jock_deleted = ["یک جوک به انتخاب کاربر حذف شد", "One joke deleted by user"]
log_1_random_jock_deleted = ["یک جوک به صورت تصادفی حذف شد", "One joke deleted randomly"]
log_jock_added = ["جوک جدید پردازش و اضافه شد", "New joke processed and added"]
log_setting = ["تنظیمات باز شد", "Settings opened"]
log_ctrl = ["تنظیمات گزارش باز شد", "Report settings opened"]
log_on = ["گزارش فعال شد", "Report activated"]
log_off = ["گزارش غیرفعال شد", "Report deactivated"]
log_user_access_failed = ["\nرمز عبور اشتباه وارد شد. تلاش دوباره برای تایید دسترسی کاربر", "\nIncorrect password entered, retrying to confirm user access"]
log_jock_reload = ["بارگذاری دوباره جوک ها انجام شد", "Jokes reloaded"]
log_some_jocks_exported = ["تعدادی جوک استخراج شد", "Some jokes exported"]
log_all_jocks_exported = ["تمام جوک ها استخراج شد", "All jokes exported"]
log_jock_reader = ["بخش خواندن جوک باز شد", "Joke reader opened"]
log_jock_adder = ["بخش اضافه کردن جوک باز شد", "Joke adder opened"]
log_jock_deleter = ["بخش حذف جوک باز شد", "Joke deleter opened"]
log_jock_exporter = ["بخش استخراج حوک باز شد", "Joke exporter opened"]
log_after_jokes = ["پایان کار. در انتظار دستور جدید", "Work finished, waiting for new command"]
jock_saver = ["ذخیره دوباره جوک ها در دیتابیس انجام شد"]
log_crash = ["برنامه مشکل پیدا کرد! برنامه در حال حاضر با یک خطا مواجه است\nدر حال ارسال ایمیل به پشتیبانی، لطفا صبر کنید", "Program was crashed! The program is currently experiencing an error\nSending email to support, please wait"]
#endregion Logs
#endregion Text
