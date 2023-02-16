import calendar
import datetime
import csv

file = open('events.csv')  # Το αρχείο που περιέχει τα γεγονότα σε μορφή csv.
csvreader = csv.reader(file)
header = next(csvreader)
events = []  # [['2022-12-4', '13:30', '60', 'Python course'], ['2022-12-5', '13:31', '90', 'Event 2']]
for x in csvreader:
    events.append(x)
is_event = []  # [['2022-12-4', 1], ['2022-12-5', 1]]
for line in events:
    i = 0
    for date in events:
        if line[0] == date[0]:
            i += 1
    is_event.append([line[0], i])


class Month:
    def __init__(self):
        """Αντλείται το τρέχον έτος, ο μήνας και η ημέρα σε μορφή yyyy, mm, dd."""
        # Το datetime.datetime.today() έχει την μορφή 2023-02-15 08:31:22.206705
        self.year = int(str(datetime.datetime.today()).split("-")[0])  # Τρέχον έτος.
        self.month = int(str(datetime.datetime.today()).split("-")[1])  # Τρέχον μήνας.
        self.day = int(str(datetime.datetime.today()).split("-")[2][0:2])  # Τρέχον ημέρα.

    def last_month(self, j, current_year, current_month):
        """Εάν ο τρέχον μήνας είναι ο Ιανουάριος, τότε ο προϊγούμενος μήνας
        είναι ο Δεκέμβριος του προϊγούμενου έτους, σε οποιαδήποτε άλλη
        περίπτωση για να βρούμε τον προϊγούμενο μήνα αφαιρείται μία μονάδα
        από τον τρέχον μήνα."""
        if current_month == 1:
            # Το calendar.monthcalendar(year, month) έχει την μορφή [[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 31, 0, 0, 0, 0, 0]]
            if calendar.monthcalendar(current_year - 1, 12)[-1][j] != 0:
                print(f"   {calendar.monthcalendar(current_year - 1, 12)[-1][j]} |", end="")
                return month.last_month(j + 1, current_year, current_month)
            else:  # Για να αποφευχθούν οι άσκοπες επαναλήψεις.
                return
        else:
            if calendar.monthcalendar(current_year, current_month - 1)[-1][j] != 0:
                print(f"   {calendar.monthcalendar(current_year, current_month - 1)[-1][j]} |", end="")
                return month.last_month(j + 1, current_year, current_month)
            else:  # Για να αποφευχθούν οι άσκοπες επαναλήψεις.
                return

    def next_month(self, j, current_year, current_month):
        """Εάν ο τρέχον μήνας είναι Δεκέμβριος, τότε ο προϊγούμενος μήνας
        είναι ο Ιανουάριος του προϊγούμενου έτους, σε οποιαδήποτε άλλη
        περίπτωση για να βρούμε τον προϊγούμενο μήνα προστίθεται μία μονάδα
        στον τρέχον μήνα."""
        if current_month == 12:
            # Το calendar.monthcalendar(year, month) έχει την μορφή [[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 31, 0, 0, 0, 0, 0]]
            if calendar.monthcalendar(current_year + 1, 1)[0][j] != 0 and j <= 5:
                print(f"    {calendar.monthcalendar(current_year + 1, 1)[0][j]} |", end="")
                return month.next_month(j + 1, current_year, current_month)
            elif j == 6:  # Τελευταία επανάληψη.
                print(f"    {calendar.monthcalendar(current_year + 1, 1)[0][j]}")
                return
            return month.next_month(j + 1, current_year, current_month)
        else:
            if calendar.monthcalendar(current_year, current_month + 1)[0][j] != 0 and j <= 5:
                print(f"    {calendar.monthcalendar(current_year, current_month + 1)[0][j]} |", end="")
                return month.next_month(j + 1, current_year, current_month)
            elif j == 6:  # Τελευταία επανάληψη.
                print(f"    {calendar.monthcalendar(current_year, current_month + 1)[0][j]}")
                return
            return month.next_month(j + 1, current_year, current_month)


def anazitisi(current_year, current_month):
    print("=== Αναζήτηση γεγονότων ====")
    year_anaz = input("Εισάγετε έτος:")
    month_anaz = input("Εισάγετε μήνα:")
    events_anaz(year_anaz, month_anaz)
    input("Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού:")
    calendar_page(current_year, current_month)
    main_menu(current_year, current_month)


def events_anaz(year_anaz, month_anaz):
    """Η λίστα lines περιέχει κάθε event/σειρά σε ξεχωριστό string.
     Η μορφή κάθε γραμμής της λίστας lines είναι για παράδειγμα:
     2022-12-4,13:30,60,Python course και η πρώτη γραμμή δείχνει
     το τι αντιπροσωπεύει κάθε στοιχείο επόμενης γραμμής."""
    # Η λήστα lines έχει την μορφή [['2023-12-31', '23:59', '0', "New Year's Eve"], ['2023-12-25', '12:0', '60', 'Christmas']]
    lines = events
    # Η μεταβλητή counter είναι ο αριθμός που εκτυπώνεται μπροστά
    # από το γεγονός και τα τακτοποίηση σε αριθμημένη λίστα.
    counter = -1
    i = -1
    # Μέσα απο την επανάληψη εκτυπώνονται όποια στοιχεία
    # ταιριάζουν στον χρόνο και μήνα που έχει δώσει ο χρήστης.
    for event in lines:
        i += 1
        if str(lines[i]).split("-")[0][2:] == year_anaz and str(lines[i]).split("-")[1] == month_anaz:
            counter += 1
            print(f"{counter}. [{str(lines[i]).split(',')[-1][2:-2]}] -> Date: {str(lines[i]).split(',')[0][2:-1]}, Time: {str(lines[i]).split(',')[1][2:-1]}, Duration: {str(lines[i]).split(',')[2][2:-1]}")
            if i == len(lines) - 1:  # Για να αποφευχθεί η υπερχείλιση στην λίστα.
                break


# Ημερολόγιο
def calendar_page(current_year, current_month):
    print(f"""
―――――――――――――――――――――――――――――――――――――――――――――――――
{months[current_month]}    {current_year}
_________________________________________________
  ΔΕΥ |  ΤΡΙ |  ΤΕΤ |  ΠΕΜ |  ΠΑΡ |  ΣΑΒ |  ΚΥΡ

""", end="")
    # Σε περίπτωση που δεν χρειάζεται να εμφανιστούν
    # οι μέρες του προϊγούμενου μήνα.
    if calendar.monthcalendar(current_year, current_month)[0][0] == 0:
        month.last_month(0, current_year, current_month)
    # Δείκτης που μετρά της εβδομάδες.
    i = -1
    for week in calendar.monthcalendar(current_year, current_month):
        i += 1
        # Δείκτης που μετρά της ημέρες μιας εβδομάδας.
        day_counter = 0
        for day in calendar.monthcalendar(current_year, current_month)[i]:
            day_counter += 1
            # Αν η ημέρα ανήκει στον τρέχον μήνα.
            if day != 0:
                # Η λογική μεταβλητή flag δείχνει αν η ημέρα έχει κάποιο γεγονός ή όχι.
                flag = False
                # Αν είναι η τελευταία μέρα της εβδομάδας.
                if day_counter == 7:
                    for event in is_event:
                        # Η μεταβλητή is_event έχει την μορφή [['2022-12-4', 1], ['2022-12-5', 1]]
                        if event[0] == f"{current_year}-{current_month}-{day}":
                            # Υπολογισμός κενού ανάμεσα στις αγκύλες
                            # και στο νούμερο της ημέρας.
                            flag = True
                            if day < 10:
                                print(f"[ *{day}]")
                            else:
                                print(f"[*{day}]")
                            break  # Για να αποφευχθούν οι άσκοπες επαναλήψεις.
                    if not flag:
                        # Υπολογισμός κενού ανάμεσα στις αγκύλες
                        # και στο νούμερο της ημέρας.
                        if day < 10:
                            print(f"[  {day}]")
                        else:
                            print(f"[ {day}]")
                else:
                    for event in is_event:
                        if event[0] == f"{current_year}-{current_month}-{day}":
                            # Υπολογισμός κενού ανάμεσα στις αγκύλες
                            # και στο νούμερο της ημέρας.
                            flag = True
                            if day < 10:
                                print(f"[ *{day}] |", end="")
                            else:
                                print(f"[*{day}] |", end="")
                            break  # Για να αποφευχθούν οι άσκοπες επαναλήψεις.
                    if not flag:
                        # Υπολογισμός κενού ανάμεσα στις αγκύλες
                        # και στο νούμερο της ημέρας.
                        if day < 10:
                            print(f"[  {day}] |", end="")
                        else:
                            print(f"[ {day}] |", end="")
        # Αν δεν χρειάζεται να εμφανιστούν οι μέρες του
        # επόμενου μήνα τότε να αλλάξει σειρά.
        if calendar.monthcalendar(current_year, current_month)[i][-1] != 0:
            print("\n")
    # Σε περίπτωση που δεν χρειάζεται να εμφανιστούν
    # οι μέρες του επόμενου μήνα.
    if calendar.monthcalendar(current_year, current_month)[-1][-1] == 0:
        month.next_month(0, current_year, current_month)


# Κυρίως μενού
def main_menu(current_year, current_month):
    print("""
_________________________________________________
Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις
παρακάτω επιλογές:
    "-" για πλοήγηση στον προηγούμενο μήνα
    "+" για διαχείριση των γεγονότων του ημερολογίου
    "*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα""")
    answer = input("    -> ")
    if answer == "q":
        # Ανοίγει για εγγραφή ('w') το αρχείο events.csv με κωδικοποίηση UTF8
        file = open('events.csv', 'w', encoding='UTF8', newline='')
        # Δημιουργεί ένα αντικείμενο writer
        writer = csv.writer(file)
        # Γράφει στο csv την επικεφαλίδα
        writer.writerow(header)
        # Γράφει στο csv κάθε εμφωλευμένη λίστα του events σε μια νέα γραμμή μέσω της μεθόδου writerows()
        writer.writerows(events)
        quit()
    elif answer == "":  # Αν η απάντηση του χρήστη είναι ENTER.
        # Αν ο τρέχον μήνας είναι ο Δεκέμβριος, τότε ο επόμενος
        # μήνας θα είναι ο Ιανουάριος του επόμενου έτους.
        if current_month == 12:
            calendar_page(current_year + 1, 1)
            main_menu(current_year + 1, 1)
        else:  # Αλλιώς προστίθεται μία μονάδα στον τρέχον μήνα.
            calendar_page(current_year, current_month + 1)
            main_menu(current_year, current_month + 1)
    elif answer == "-":
        # Αν ο τρέχον μήνας είναι ο Ιανουάριος, τότε ο προϊγούμενου
        # μήνας είναι ο Δεκέμβριος του προϊγούμενου έτους.
        if current_month == 1:
            calendar_page(current_year - 1, 12)
            main_menu(current_year - 1, 12)
        else:  # Αλλιώς αφαιρείται μία μονάδα από τον τρέχον μήνα.
            calendar_page(current_year, current_month - 1)
            main_menu(current_year, current_month - 1)
    elif answer == "*":
        anazitisi(current_year, current_month)
    elif answer == "+":
        opt_management(current_year, current_month)
    else:
        calendar_page(current_year, current_month)
        main_menu(current_year, current_month)


def opt_management(current_year, current_month):
    """Υλοποιεί το μενού διαχείρισης γεγονότων με έλεγχο εγκυρότητας ώστε να επιλέγεται σωστή επιλογή."""
    print('----------------------------------------------------')
    print('Διαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:')
    opt_1 = '1 Καταγραφή νέου γεγονότος'
    opt_2 = '2 Διαγραφή γεγονότος'
    opt_3 = '3 Ενημέρωση γεγονότος'
    opt_0 = '0 Επιστροφή στο κυρίως μενού' 
    error_message = 'Δώσατε λανθασμένη ενέργεια. Παρακαλώ επιλέξτε ενέργεια.'
    while True:
        selection = input(opt_1 + '\n' + opt_2 + '\n' + opt_3 + '\n' + opt_0 + '\n' + '-> ')
        if selection == '0':
            opt0(current_year, current_month)
        elif selection == '1':
            opt1(current_year, current_month)
        elif selection == '2': 
            opt2(current_year, current_month)
        elif selection == '3':
            opt3(current_year, current_month)
        else:
            print(error_message)


def date_inp():
    """Εισάγει με έλεγχο εγκυρότητας ημερομηνία από τον χρήστη ώστε να είναι πραγματική
    ημερομηνία και το έτος να είναι μεγαλύτερο του 2022, σε μορφή ΥΥΥΥ-ΜΜ-DD."""
    while True:
        valid = True
        error_message = 'Δώσατε λανθασμένη ημερομηνία.'
        date = input('Δώσε ημερομηνία γεγονότος σε μορφή ΥΥΥΥ-ΜΜ-DD' + '\n' + '-> ')
        if date[0:3].isdigit() and date[4] == date[7] == '-' and date[5:6].isdigit() and date[-2:].isdigit:
            year, month, day = date.split('-')  # Χωρίζει το string όταν υπάρχει παύλα.
            year, month, day = int(year), int(month), int(day)
            if year > 2022:
                # Ελέγχει αν η ημερομηνία είναι πραγματική.
                # Εάν η ημερομηνία δεν είναι πραγματική (περίπτωση ValueError)
                # κάνει την τιμή της 'σημαίας' valid False.
                try:
                    datetime.datetime(year, month, day)
                except ValueError:
                    valid = False
            else:
                valid = False
        else:
            valid = False
        if valid:
            return str(year) + '-' + str(month) + '-' + str(day)
        else:
            print(error_message)


def time_inp():
    """Εισάγει με έλεγχο εγκυρότητας ημερομηνία από τον χρήστη ώστε
    να είναι πραγματική ώρα γεγονότος, σε μορφή HH:MM."""
    error_message = 'Δώσατε λανθασμένη ώρα.'
    while True:
        time = input('Δώστε ώρα γεγονότος σε μορφή HH:MM' + '\n' + '-> ')
        if time[0:1].isdigit() and time[3:4].isdigit() and time[2] == ':':
            hour, minute = time.split(':')
            hour, minute = int(hour), int(minute)
            if hour in range(24) and minute in range(60):  # Έλεγχει αν η ώρα λαμβάνει τιμές 0-23 και τα λεπτά τιμές 0-59.
                return str(hour) + ':' + str(minute)
            else:
                print(error_message)
        else:
            print(error_message)


def duration_inp():
    error_message = 'Δώσατε λανθασμένη διάρκεια.'
    while True:
        duration = input('Δώστε διάρκεια γεγονότος' + '\n' + '-> ')
        if duration.isdigit():
            duration = int(duration)
            if duration > 0:
                return str(duration)
            else:
                print(error_message)
        else:
            print(error_message)


def title_inp():
    """Εισάγει το τίτλος γεγονότος με έλεγχο εγκυρότητας ώστε
    να είναι string και να μην περιέχει το χαρακτήρα ,"""
    error_message = 'Δώσατε λανθασμένο τίτλο.'
    while True:
        title = input('Δώστε τίτλο γεγονότος' + '\n' + '-> ')
        if ',' not in title:
            return title
        else:
            print(error_message)


def opt1(current_year, current_month):
    """Υλοποιεί την επιλόγη 1 με την βοήθεια των συναρτήσεων date_inp, time_inp, duration_inp, title_inp.
    Δηλαδή ζητά διαδοχικά όλα τα στοιχεία ενός νέου γεγονότος, θα δημιουργεί το γεγονός και θα το προσθέτει
    στη λίστα των γεγονότων. Στο τέλος επιστρέφει στο μενού διαχείρισης γεγονότων."""
    date = date_inp()
    time = time_inp()
    duration = duration_inp()
    title = title_inp()
    events.append([date, time, duration, title])
    event_dates = [event[0] for event in is_event]
    if date in event_dates:
        index = event_dates.index(date)
        is_event[index] = [date, is_event[index][1] + 1]
    else:
        is_event.append([date, 1])
    opt_management(current_year, current_month)


def events_search(year_anaz, month_anaz):
    """Η λίστα lines περιέχει κάθε event/σειρά σε ξεχωριστό string.
     Η μορφή κάθε γραμμής της λίστας lines είναι για παράδειγμα:
     2022-12-4,13:30,60,Python course και η πρώτη γραμμή δείχνει
     το τι αντιπροσωπεύει κάθε στοιχείο επόμενης γραμμής."""
    # Η λήστα lines έχει την μορφή [['2023-12-31', '23:59', '0', "New Year's Eve"], ['2023-12-25', '12:0', '60', 'Christmas']]
    lines = events
    # Η λίστα ls περιλαμβάνει όλα τα events που πληρούν τα κριτήρια της αναζήτησης
    ls = []
    # Η μεταβλητή counter είναι ο αριθμός που εκτυπώνεται μπροστά
    # από το γεγονός και τα τακτοποίηση σε αριθμημένη λίστα.
    counter = -1
    i = -1
    # Μέσα απο την επανάληψη εκτυπώνονται όποια στοιχεία
    # ταιριάζουν στον χρόνο και μήνα που έχει δώσει ο χρήστης.
    for event in lines:
        i += 1
        if str(lines[i]).split("-")[0][2:] == str(year_anaz) and str(lines[i]).split("-")[1] == str(month_anaz):
            counter += 1
            ls.append(events[i])
            print(f"{counter}. [{str(lines[i]).split(',')[-1][2:-2]}] -> Date: {str(lines[i]).split(',')[0][2:-1]}, Time: {str(lines[i]).split(',')[1][2:-1]}, Duration: {str(lines[i]).split(',')[2][2:-1]}")
            if i == len(lines) - 1:  # Για να αποφευχθεί η υπερχείλιση στην λίστα.
                break
    return ls


def year_inp():
    """Εισάγεται το έτος του γεγονότος προς διαγραφή με έλεγχο
    εγκυρότητας 'ωστε να είναι ακέραιος μεγαλύτερος του 2022."""
    error_message = 'Δώσατε λανθασμένο έτος γεγονότος .'
    while True:
        year = input('Δώστε έτος γεγονότος.' + '\n' + '->')
        if year.isdigit():
            year = int(year)
            if year > 2022:
                return year
            else:
                print(error_message)
        else:
            print(error_message)


def month_inp():
    """Εισάγεται o μήνας του γεγονότος προς διαγραφή με έλεγχο
    εγκυρότητας ωστε να είναι ακέραιος και 1 <= month <= 12."""
    error_message = 'Δώσατε λανθασμένο μήνα γεγονότος.'
    while True:
        month = input('Δώστε μήνα γεγονότος.' + '\n' + '->')
        if month.isdigit():
            month = int(month)
            if month in range(1, 13):
                return month
            else:
                print(error_message)
        else:
            print(error_message)


def opt2(current_year, current_month):
    """Υλοποιεί την επιλόγη 2 με την βοήθεια των συναρτήσεων year_inp, month_inp, events_search. Γίνεται είσοδος έγκυρου έτους
    και μήνα από το χρήστη και στην συνέχεια γίνεται αναζήτηση γεγονότων με βάση συγκεκριμένο μήνα όπου  εμφανίζεται αριθμημένη
    λίστα με τα γεγονότα του μήνα έπειτα ο χρήστης καλείται να δώσει τον αριθμό του γεγονότος προς διαγραφή."""
    if len(events) > 0:  # Ελέχει εάν υπάρχουν γεγονότα καταχωρημένα.
        year = year_inp()  
        month = month_inp()
        month_events = events_search(year, month)
        flag = len(month_events)
        if flag > 0:  # Ελέγχει εάν υπάρχουν γεγονότα καταχωρημένα για τον μήνα.
            error_message = 'Δώσατε λανθασμένο αριθμό γεγονότος προς διαγραφή.'
            while True:
                key = input('Δώστε αριθμό γεγονότος προς διαγραφή: ')
                if key.isdigit():
                    key = int(key)
                    if 0 <= key <= flag:
                        events.remove(month_events[key])
                        date = month_events[key][0]
                        # Η μεταβλητή i είναι το index της λήστας is_event και
                        # αυξάνεται κατά μια μονάδα σε κάθε επανάληψη.
                        i = -1
                        # Η λήστα is_event έχει την μορφή [['2022-12-4', 1], ['2022-12-5', 2], ['2022-12-31', 1]]
                        # όπου το πρώτο μέρος είναι η ημερομηνία του γεγονότος και το δεύτερο είναι ο αριθμός γεγονότων.
                        for event in is_event:
                            i += 1
                            if event[0] == date:
                                is_event[i] = [date, event[1] - 1]
                                if event[1] == 0:
                                    is_event.remove(event)
                                break
                        break
                    else:
                        print(error_message)
                else:
                    print(error_message)
        else:
            print('Δεν υπάρχει κανένα γεγονός καταχωρημένο τον μήνα που επιλέξατε.')                
    else:
        print('Δεν υπάρχει κανένα γεγονός καταχωρημένο.')
    opt_management(current_year, current_month)


def opt3(current_year, current_month):
    """ Υλοποιεί την επιλόγη 3 με την βοήθεια των συναρτήσεων year_inp, month_inp, change_date, change_time, change_duration,change_title.
    Γίνεται είσοδος έγκυρου έτους και μήνα από το χρήστη και στην συνέχεια γίνεται αναζήτηση γεγονότων με βάση συγκεκριμένο μήνα όπου  
    εμφανίζεται αριθμημένη λίστα με τα γεγονότα του μήνα έπειτα ο χρήστης καλείται να δώσει τον αριθμό του γεγονότος προς ενημέρωση.
    Έπειτα ζητείται η νέα τιμή του κάθε στοιχείου. Αν δεν εισαχθεί κάποια τιμή τότε διατηρείται η αρχική."""
    def change_date(ls):
        """Δέχεται σαν είδοδο ένα γεγονός σε μορφή λίστας και δίνει ως έξοδο μια νέα ημερομηνία για το γεγονός."""
        while True:
            valid = True
            error_message = 'Δώσατε λανθασμένη ημερομηνία.'
            date = input('\n' + 'Ημερομηνία γεγονότος ' + '(' + str(ls[0]) + '):')
            if date == '':
                return ls[0]
            elif date[0:3].isdigit() and date[4] == date[7] == '-' and date[5:6].isdigit() and date[-2:].isdigit:
                year, month, day = date.split('-')  # Χωρίζει το string όταν υπάρχει παύλα.
                year, month, day = int(year), int(month), int(day)
                if year > 2022:
                    # Ελέγχει αν η ημερομηνία είναι πραγματική.
                    # Εάν η ημερομηνία δεν είναι πραγματική (περίοπτωση ValueError)
                    # κάνει την τιμή της 'σημαίας' valid False.
                    try:
                        datetime.datetime(year, month, day)
                    except ValueError:
                        valid = False
                else:
                    valid = False
            else:
                valid = False
            if valid:
                return str(year) + '-' + str(month) + '-' + str(day) 
            else:
                print(error_message)

    def change_time(ls):
        """Δέχεται σαν είδοδο ένα γεγονός σε μορφή λίστας και δίνει ως έξοδο μια νέα ώρα για το γεγονός."""
        error_message = 'Δώσατε λανθασμένη ώρα.'
        while True:
            time = input('Ώρα γεγονότος ' + '(' + str(ls[1]) + '):')
            if time == '':
                return ls[1]
            elif time[0:1].isdigit() and time[3:4].isdigit() and time[2] == ':':
                hour, minute = time.split(':')
                hour, minute = int(hour), int(minute)
                if hour in range(24) and minute in range(60):
                    return time
                else:
                    print(error_message)
            else:
                print(error_message)

    def change_duration(ls):
        """Δέχεται σαν είδοδο ένα γεγονός σε μορφή λίστας και δίνει ως έξοδο μια νέα διάρκεια για το γεγονός."""
        error_message = 'Δώσατε λανθασμένη διάρκεια.'
        while True:
            duration = input('Διάρκεια γεγονότος ' + '(' + str(ls[2]) + '):')
            if duration == '':
                return ls[2]
            elif duration.isdigit() and duration != '0':
                return duration
            else:
                print(error_message)

    def change_title(ls):
        """Δέχεται σαν είδοδο ένα γεγονός σε μορφή λίστας και δίνει ως έξοδο ένα νέο τίτλο για το γεγονός."""
        error_message = 'Δώσατε λανθασμένο τίτλο.'
        while True:
            title = input('Τίτλος γεγονότος ' + '(' + ls[3] + '):')
            if title == '':
                return ls[3]
            elif ',' not in title:
                return title
            else:
                print(error_message)
    year = year_inp()
    month = month_inp()
    if len(events) > 0:
        month_events = events_search(year, month)
        flag = len(month_events)
        if flag > 0:
            error_message = 'Δώσατε λανθασμένο αριθμό γεγονότος προς ενημέρωση.'
            while True:
                key = input('Επιλέξτε γεγονός προς ενημέρωση:')
                if key.isdigit():
                    key = int(key)
                    if 0 <= key <= flag:
                        events.remove(month_events[key])
                        date = month_events[key][0]
                        # Η μεταβλητή i είναι το index της λήστας is_event και
                        # αυξάνεται κατά μια μονάδα σε κάθε επανάληψη.
                        i = -1
                        # Η λήστα is_event έχει την μορφή [['2022-12-4', 1], ['2022-12-5', 2], ['2022-12-31', 1]]
                        # όπου το πρώτο μέρος είναι η ημερομηνία του γεγονότος και το δεύτερο είναι ο αριθμός γεγονότων.
                        for event in is_event:
                            i += 1
                            if event[0] == date:
                                is_event[i] = [date, event[1] - 1]
                                if event[1] == 0:
                                    is_event.remove(event)
                                break
                        event = month_events[key]
                        new_date = change_date(event)
                        event[0] = new_date
                        new_time = change_time(event)
                        event[1] = new_time
                        new_duration = change_duration(event)
                        event[2] = new_duration
                        new_title = change_title(event)
                        event[3] = new_title
                        events.append(event)
                        event_dates = [event[0] for event in is_event]
                        if date in event_dates:
                            index = event_dates.index(date)
                            is_event[index] = [date, is_event[index][1] + 1]
                        else:
                            is_event.append([date, 1])
                        break
                    else:
                        print(error_message)
                else:
                    print(error_message)
            print('\n' + '\n' + 'Το γεγονός ενημερώθηκε: <[' + new_title + '] -> Date: ' + str(new_date) + ', Time: ' + str(new_time) + ', Duration: ' + str(new_duration))
    opt_management(current_year, current_month)


def opt0(current_year, current_month):
    """Υλοποιεί την επιλογή 0, δηλαδή επιστρέφει στο κυρίως μενού της εφαρμογής, με προβολή
    του μήνα που εμφανιζόταν πριν την ενεργοποίηση της επιλογής (+) για διαχείριση γεγονότων."""
    calendar_page(current_year, current_month)
    main_menu(current_year, current_month)


def notifications(current_full_day):
    for event in events:
        if event[0] == current_full_day:
            current_time = str(datetime.datetime.now())[11:16]  # Έχει τη φορφή 22:30.
            current_hour = current_time.split(":")[0]  # Έχει τη φορφή 22.
            current_min = current_time.split(":")[1]  # Έχει τη φορφή 30.
            dhour = int(event[1].split(":")[0]) - int(current_hour)  # Η διαφορά ωρών.
            dmin = int(event[1].split(":")[1]) - int(current_min)  # Η διαφορά λεπτών.
            print("\n")
            if dhour > 0:
                if dmin > 0:
                    print(f"Ειδοποίηση: σε {dhour} ώρες και {dmin} λεπτά από τώρα έχει προγραμματιστεί το γεγονός [{event[-1]}].")
                elif dmin == 0:
                    print(f"Ειδοποίηση: σε {dhour} ώρες από τώρα έχει προγραμματιστεί το γεγονός [{event[-1]}].")
                else:
                    print(f"Ειδοποίηση: σε {int(dhour) - 1} ώρες και {int(dmin) + 60} λεπτά από τώρα έχει προγραμματιστεί το γεγονός [{event[-1]}].")
            elif dhour == 0 and dmin > 0:
                print(f"Ειδοποίηση: σε {dmin} λεπτά από τώρα έχει προγραμματιστεί το γεγονός [{event[-1]}].")
            elif dhour == 0 and dmin == 0:
                print(f"Ειδοποίηση: τώρα έχει προγραμματιστεί το γεγονός [{event[-1]}].")
            else:
                print(f"Ειδοποίηση: νωρίτερα είχατε προγραμματίσει το γεγονός [{event[-1]}].")


def main():
    current_year = month.year  # Τρέχον χρόνος.
    current_month = month.month  # Τρέχον μήνας.
    current_day = month.day  # Τρέχον ημέρα.
    current_full_day = str(current_year) + "-" + str(current_month) + "-" + str(current_day)  # Τρέχον ημέρα σε μορφή yyyy-m-d.
    notifications(current_full_day)
    calendar_page(current_year, current_month)
    main_menu(current_year, current_month)


month = Month()
# Λεξικό το οποίο μετατρέπει το νούμερο του
# μήνα στα πρώτα τρία-τέσσερα γράμματά του.
months = {
    1: "ΙΑΝ",
    2: "ΦΕΒ",
    3: "ΜΑΡ",
    4: "ΑΠΡ",
    5: "ΜΑΪ",
    6: "ΙΟΥΝ",
    7: "ΙΟΥΛ",
    8: "ΑΥΓ",
    9: "ΣΕΠ",
    10: "ΟΚΤ",
    11: "ΝΟΕ",
    12: "ΔΕΚ"
}

if __name__ == "__main__":
    main()

# Αυτή η εργασία ήταν μέρος του μαθήματος Εισαγωγή στην Επιστήμη των Υπολογιστών στο πρώτο εξάμηνο του τμήματος
# πληροφορικής του Οικονομικού Πανεπιστημίου Αθηνών και εκπληρώθηκε από τους μαθήτες
# Γιώργος Σουλατζής και Θάνος Παναγιωτίδης.
