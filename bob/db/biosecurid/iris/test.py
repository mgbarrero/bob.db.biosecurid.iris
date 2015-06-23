#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""A few checks at the Biosecurid database.
"""

import os, sys
import unittest
import bob.db.biosecurid.iris

class BiosecuridDatabaseTest(unittest.TestCase):
  """Performs various tests on the Biosecurid database."""

  def test01_clients(self):
    db = bob.db.biosecurid.iris.Database()
    self.assertEqual(len(db.groups()), 3)
    self.assertEqual(len(db.clients()), 800)
    self.assertEqual(len(db.clients(groups='dev')), 300)
    self.assertEqual(len(db.clients(groups='eval')), 200)
    self.assertEqual(len(db.clients(groups='world')), 300)
    self.assertEqual(len(db.clients(groups='impostorDev')), 25)
    self.assertEqual(len(db.clients(groups='impostorEval')), 20)
    self.assertEqual(len(db.models()), 455)
    self.assertEqual(len(db.models(groups='dev')), 275)
    self.assertEqual(len(db.models(groups='eval')), 180)


  def test02_objects(self):
    db = bob.db.biosecurid.iris.Database()
    self.assertEqual(len(db.objects()), 12800)
    # A
    self.assertEqual(len(db.objects(protocol='A')), 12800)
    self.assertEqual(len(db.objects(protocol='A', groups='world')), 4800)
    self.assertEqual(len(db.objects(protocol='A', groups='dev')), 4800)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='enrol')), 2200)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe')), 2600)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', classes='client')), 2200)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', classes='impostor')), 400)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', model_ids=[1301])), 408)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', model_ids=[1301], classes='client')), 8)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', model_ids=[1301], classes='impostor')), 400)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', model_ids=[1301,1302])), 416)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', model_ids=[1301,1302], classes='client')), 16)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', model_ids=[1301,1302], classes='impostor')), 400)
    self.assertEqual(len(db.objects(protocol='A', groups='eval')), 3200)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='enrol')), 1440)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe')), 1760)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', classes='client')), 1440)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', classes='impostor')), 320)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1601])), 328)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1601], classes='client')), 8)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1601], classes='impostor')), 320)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1601,1602])), 336)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1601,1602], classes='client')), 16)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1601,1602], classes='impostor')), 320)






  def test03_driver_api(self):

    from bob.db.base.script.dbmanage import main
    self.assertEqual(main('biosecurid.iris dumplist --self-test'.split()), 0)
    self.assertEqual(main('biosecurid.iris dumplist --protocol=A --class=client --group=dev --purpose=enrol --client=1301 --self-test'.split()), 0)
    self.assertEqual(main('biosecurid.iris checkfiles --self-test'.split()), 0)
    self.assertEqual(main('biosecurid.iris reverse user1001/session0001/u1001s0001_ir0001 --self-test'.split()), 0)
    self.assertEqual(main('biosecurid.iris path 3011 --self-test'.split()), 0)

