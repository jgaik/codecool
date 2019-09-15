import rtmidi
import time

class Midi:
    COLOR = 69
    def __enter__(self):
        self.midiOut = rtmidi.MidiOut()
        for port_no in range(self.midiOut.get_port_count()):
            port_name = self.midiOut.get_port_name(port_no)
            if port_name.find('Launchpad Mini MIDI 1') > -1:
                self.midiPort = self.midiOut.open_port(port_no)
    
    def __exit__(self, _, __, ___):
        self.midiPort.close_port()

    def lightCell(self, posx, posy, color):
        self.midiPort.send_message([0x90, int(f"0x{posx}{posy}", 16), color])

    def lightBoard(self, board):
        for r in range(len(board)):
            for c in range(len(board[r])):
                self.lightCell(r,c,board[r][c] * self.COLOR)