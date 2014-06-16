import cairo

import base
from os import statvfs
import time

from multiprocessing import cpu_count

__all__ = [
    'CPUMon',
]

class CPUMon(base._TextBox):
    def __init__(self, **config):
        base._TextBox.__init__(self, '0', width=bar.CALCULATED, **config)
        self.timeout_add(self.update_interval, self.update)
        self.add_text = text
        self.add_defaults(CPUMon.defaults)
        self.maxvalue = 100
        self.oldvalues = self._getvalues()

    def _getvalues(self):
        with open('/proc/stat') as file:
            lines = file.readlines()
            line = lines.pop(0)
            cpus = cpu_count()

            for cpu in range(0,cpus):
                line = lines[cpu]
                if line.startswith("cpu%s" % cpu):


            # core specified, grab the corresponding line
            if isinstance(self.core, int):
                # we already removed the first line from the list,
                # so it's 0 indexed now :D
                line = lines[self.core]

                if not line.startswith("cpu%s" % self.core):
                    raise ValueError("No such core: %s" % self.core)

            name, user, nice, sys, idle, iowait, tail = line.split(None, 6)

            return (int(user), int(nice), int(sys), int(idle))
     def _update_drawer(self):
        if self.volume == -1:
            self.text = 'Null values'
        else:
            self.text = '{0}{1}'.format(self.add_text, self.volume)

    def draw(self):
        if self.theme_path:
            self.drawer.draw(self.offset, self.width)
        else:
            base._TextBox.draw(self)