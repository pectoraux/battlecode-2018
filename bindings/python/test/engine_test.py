import battlecode as bc

def test_map_location():
    loc = bc.MapLocation(bc.Planet.Earth,1,2)
    assert loc.planet == bc.Planet.Earth
    assert loc.x == 1
    assert loc.y == 2
    loc.y = 3
    assert loc.y == 3
    loc.planet = bc.Planet.Mars
    assert loc.planet == bc.Planet.Mars

def test_direction():
    assert bc.Direction.North.opposite() == bc.Direction.South
    loc = bc.MapLocation(bc.Planet.Earth,1,2)
    locne = loc.add(bc.Direction.Northeast)
    assert locne.x == 2, locne.x
    assert locne.y == 3, locne.y

def test_controller():
    c = bc.GameController.new_manager(bc.GameMap.test_map())
    print(c.start_game(bc.Player(bc.Team.Red, bc.Planet.Earth)).to_json())
