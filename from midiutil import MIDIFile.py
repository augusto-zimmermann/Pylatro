from midiutil import MIDIFile

# Create a MIDIFile object
midi_file = MIDIFile(1)  # One track

# Add a track name and tempo
track = 0
time = 0
midi_file.addTrackName(track, time, "My Melody")
midi_file.addTempo(track, time, 120)  # 120 beats per minute

# Add notes
channel = 0
volume = 100  # 0-127

# C4 note
midi_file.addNote(track, channel, 60, time, 1, volume)
time += 1

# G4 note
midi_file.addNote(track, channel, 67, time, 1, volume)
time += 1

# Write the MIDI file
with open("simple_melody.mid", "wb") as output_file:
    midi_file.writeFile(output_file)