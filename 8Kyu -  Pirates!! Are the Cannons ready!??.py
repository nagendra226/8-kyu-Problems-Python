def cannons_ready(gunners):
  # Fire! or Shiver me timbers!
    count_aye = 0
    length_gunners = len(gunners)
    for key,values in gunners.items():
        if values == 'aye':
            count_aye = count_aye + 1
    if count_aye == length_gunners:
        return 'Fire!'
    else:
        return 'Shiver me timbers!'
