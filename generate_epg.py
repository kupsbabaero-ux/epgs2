import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

def create_epg():
    tv = ET.Element("tv", generator_info_name="Auto EPG Generator")

    # Add Channel
    channel = ET.SubElement(tv, "channel", id="KapamilyaChannel.ph")
    display_name = ET.SubElement(channel, "display-name")
    display_name.text = "Kapamilya Channel"

    # 1. MONDAY TO FRIDAY SCHEDULE
    weekday_schedules = [
        ("05", "30", "06", "00", "Kapamilya Daily Mass", "Daily morning mass celebration."),
        ("06", "00", "07", "00", "School Anywhere", "Educational program by Knowledge Channel."),
        ("07", "00", "07", "30", "The Flying House", "Animated Bible stories for kids."),
        ("07", "30", "08", "00", "Superbook Reimagined", "3D animated Bible series."),
        ("08", "00", "10", "00", "Blockbusters sa Umaga", "Morning movie block featuring hit films."),
        ("10", "00", "11", "00", "Oh My Gan!", "Variety/Entertainment show."),
        ("11", "00", "12", "00", "Face to Face with Ate Koring", "Public service talk show."),
        ("12", "00", "14", "30", "It's Showtime", "Noontime variety and talent show."),
        ("14", "30", "15", "15", "My Bespren Emman", "Afternoon drama series."),
        ("15", "15", "16", "00", "Can't Buy Me Love", "Romantic drama series."),
        ("16", "00", "16", "45", "High Street", "Youth drama and thriller series."),
        ("16", "45", "17", "30", "Happiness", "KDrama series dubbed in Tagalog."),
        ("17", "30", "17", "45", "TV Patrol Express", "Quick summary of top news stories."),
        ("17", "45", "18", "30", "Minute to Win It", "Game show hosted by Luis Manzano."),
        ("18", "30", "20", "00", "TV Patrol", "Flagship news program of ABS-CBN."),
        ("20", "00", "20", "45", "FPJ's Batang Quiapo", "Action drama starring Coco Martin."),
        ("20", "45", "21", "30", "Sigabo / Primetime Drama", "ABS-CBN Primetime Bida drama series."),
        ("21", "30", "22", "15", "Someone, Someday", "Kapamilya romance-drama series."),
        ("22", "15", "22", "45", "The World Tonight", "Late-night news broadcast."),
        ("22", "45", "23", "59", "Movie Central Presents", "Late night movie feature.")
    ]

    # 2. SATURDAY SCHEDULE
    saturday_schedules = [
        ("05", "30", "06", "00", "Kapamilya Daily Mass", "Saturday morning mass celebration."),
        ("06", "00", "07", "00", "Bayan Mo, Ipatrol Mo", "Public service and citizen journalism."),
        ("07", "00", "08", "00", "Superbook", "Animated kids program."),
        ("08", "00", "10", "00", "Kapamilya Blockbusters Weekend", "Saturday morning movie special."),
        ("10", "00", "12", "00", "It's Showtime Saturday", "Extended weekend noontime variety show."),
        ("12", "00", "14", "30", "It's Showtime Continuation", "Live performances and segments."),
        ("14", "30", "16", "00", "Ipaglaban Mo", "Legal drama anthology hosted by Atty. Jose and Jopet Sison."),
        ("16", "00", "17", "00", "Soco: Scene of the Crime Operatives", "Investigative documentary program."),
        ("17", "00", "18", "00", "TV Patrol Weekend", "Weekend news wrap-up."),
        ("18", "00", "19", "15", "Goin' Bulilit", "Kiddie gag show."),
        ("19", "15", "20", "45", "The Voice Kids / Reality Show", "Weekend reality competition show."),
        ("20", "45", "21", "45", "Maalaala Mo Kaya (Classic/Special)", "Drama anthology series."),
        ("21", "45", "23", "30", "Kapamilya Action Movie", "Late night Saturday action block.")
    ]

    # 3. SUNDAY SCHEDULE
    sunday_schedules = [
        ("06", "00", "07", "00", "The Healing Eucharist", "Sunday Holy Mass."),
        ("07", "00", "08", "00", "Kabuhayang Swak na Swak", "Livelihood and business show."),
        ("08", "00", "10", "00", "Sunday Blockbusters", "Family weekend movie block."),
        ("10", "00", "12", "00", "ASAP Natin 'To Prep Show", "Pre-show coverage and countdowns."),
        ("12", "00", "14", "15", "ASAP Natin 'To", "Flagship Sunday musical variety show."),
        ("14", "15", "16", "00", "Sunday Mega Movie", "Afternoon movie presentation."),
        ("16", "00", "17", "00", "Rated Korina / KBYN", "Magazine and news feature show."),
        ("17", "00", "18", "00", "TV Patrol Weekend", "Sunday evening news broadcast."),
        ("18", "00", "19", "30", "Goin' Bulilit / Weekend Special", "Family weekend comedy show."),
        ("19", "30", "21", "00", "The Voice / Weekend Prime", "Sunday primetime talent reality show."),
        ("21", "00", "22", "30", "Kapamilya Sunday Cinema", "Late night Sunday blockbusters."),
        ("22", "30", "23", "30", "Sunday's Best", "Documentaries and special events.")
    ]

    # Loop for 7 days starting today
    today = datetime.now()
    for i in range(7):
        target_date = today + timedelta(days=i)
        date_str = target_date.strftime("%Y%m%d")
        day_of_week = target_date.weekday() # 0=Mon, 1=Tue, ..., 5=Sat, 6=Sun

        # Piliin ang tamang schedule batay sa araw
        if day_of_week == 5:
            current_schedule = saturday_schedules
        elif day_of_week == 6:
            current_schedule = sunday_schedules
        else:
            current_schedule = weekday_schedules

        # Generate XML programmes para sa araw na ito
        for s_h, s_m, e_h, e_m, title, desc in current_schedule:
            start_time = f"{date_str}{s_h}{s_m}00 +0800"
            end_time = f"{date_str}{e_h}{e_m}00 +0800"

            programme = ET.SubElement(tv, "programme", {
                "start": start_time,
                "stop": end_time,
                "channel": "KapamilyaChannel.ph"
            })

            title_elem = ET.SubElement(programme, "title", lang="en")
            title_elem.text = title

            desc_elem = ET.SubElement(programme, "desc", lang="en")
            desc_elem.text = desc

    # Write output XML
    tree = ET.ElementTree(tv)
    ET.indent(tree, space="  ", level=0)
    tree.write("epg.xml", encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    create_epg()
