# -*- coding: UTF-8 -*-
""" module ncc1701: getting Python ready for the
    enterprise
    """
"""
Copyright (c) 2008 HaraldArminMassa, GHUM Harald Massa

haraldarminmassa@mail.com

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""



__all__=["Beam", "Phaser", "reroute_power", "PhaserNotLockedOnTarget",
               "Shields","WarpEngine", "AuthorizationRequired",
               "WrongAuthorization", "TractorBeam",
                ]

import exceptions
class BeamNotLockedOnTarget (exceptions.BaseException):
    def __init__(self, obj):
        self.beam = obj
    
    def __str__(self):
        return "%s not locked on target!" % (self.beam,)


class TractorBeamStillActive(exceptions.BaseException):
    pass


class AuthorizationRequired (exceptions.BaseException):
    pass


class WrongAuthorization(exceptions.BaseException):
    pass


class Beam(object):
    def __init__(self):
        raise NotImplementedException("abstract base class")
    
    def lock_target(self, what):
        """makes where the target of any beam""" 
        self.what=what
        print self
    
    def unlock_target(self):
        """frees the beam again"""
        if self.locked:
            del self.what
    
    @property
    def locked(self):
        return getattr(self,"what",None) is not None


class Phaser(Beam):
    def __init__(self):
        """creates a new Phaser control object"""
        print "Phaser initiated"
    
    def fire(self):
        if self.locked:
            print "phaser fired on %s" % (self.what,)
        else:
            raise BeamNotLockedOnTarget(self)
    
    def __repr__(self):
        if self.locked:
            return "Phaser locked on %s" % (self.what,)
        else:
            return "Phaser"


class TractorBeam(Beam):
    def __init__(self):
        """creates a new tractor beam control object"""
        print "Tractor beam initiated"
    
    def activate(self):
        if self.locked:
            self.active = True
            print "%s captured by tractor beam" % (self.what,)
        else:
            raise BeamNotLockedOnTarget(self)
    
    def unlock_target(self):
        if getattr(self,"active",False):
            raise TractorBeamStillActive
        else:
            super(TractorBeam, self).unlock_target()
    
    def release(self):
        if self.locked and getattr(self,"active",False):
            del self.active
            print "%s released" % (self.what,)
    
    def __repr__(self):
        if self.locked:
            return "Tractor beam locked on %s" % (self.what,)
        else:
            return "Tractor beam"


def reroute_power(from_what, to_what):
    """reroutes power from from_what to to_what"""
    print "rerouting power from %s to %s" % (from_what, to_what)
    
    
class WarpEngine(object):
    def eject_core(self, authorization=None):
        """ejects the Warp-core. use with caution and proper authorization"""
        if authorization is None:
            raise AuthorizationRequired
        elif authorization == "Kirk":
            print "ejecting Warp core, prepare to abandon ship"
        else:
            raise WrongAuthorization
    
    def __repr__(self):
        return "WarpEngine %s " % (id(self),)


class ImpulseEngine(object):
    def activate(self):
        """activates the impulse engine."""
        print "impulse engine activated."    
  
    def __repr__(self):
        return "ImpulseEngine %s " % (id(self),)
  

class Shields(object):
    def __repr__(self):
        return "Shields %s " % (id(self),)
    

class Hull(object):
    def emergency_separation(self, authorization=None):
        """separates the primary (aka. saucer) and secondary hulls in case of an emergency."""
        if authorization is None:
            raise AuthorizationRequired
        elif authorization == "Kirk":
            print "separating saucer section, please prepare for leaving secondary hull!"
        else:
            raise WrongAuthorization
        
        impulseEngine = ImpulseEngine()
        impulseEngine.activate()
        
    def __repr__(self):
        return "Hull %s " % (id(self),)
    

if __name__=='__main__':
    pass

