import xml.etree.ElementTree as ET
import os


def create_md_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(content))

def get_text_or_default(element, default_value=''):
    return element.text if element is not None else default_value

def get_attribute_or_default(element, attribute, default_value=''):
    if element is not None:
        if attribute in element.attrib:
            return element.get(attribute)
        elif element.text is not None:
            return element.text
    return default_value

def parse_planets_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    stars_data = []

    for star_elem in root.findall('.//star'):
        counter=0;
        star_info = {
            'name': get_attribute_or_default(star_elem, 'name'),
            'blackHole': get_attribute_or_default(star_elem, 'blackHole', default_value='false') == 'true',
            'numGasGiants': get_attribute_or_default(star_elem, 'numGasGiants', default_value='0'),
            'numPlanets': get_attribute_or_default(star_elem, 'numPlanets', default_value='0'),
            'size': get_attribute_or_default(star_elem, 'size', default_value='1.0'),
            'temp': get_attribute_or_default(star_elem, 'temp', default_value='100'),
            'x': get_attribute_or_default(star_elem, 'x', default_value='0'),
            'y': get_attribute_or_default(star_elem, 'y', default_value='0'),
            'planets': [],
        }

        if counter == 0:
            planet_info = {
                'moons': [],
            }

        for planet_elem in star_elem.findall('.//planet'):
            if planet_elem is not None:
                if counter == 0 or planet_elem not in planet_info['moons']:
                    counter = 1
                    planet_info = {
                        'name': get_attribute_or_default(planet_elem, 'name'),
                        'DIMID': get_attribute_or_default(planet_elem, 'DIMID', default_value='0'),
                        'customIcon': get_attribute_or_default(planet_elem, 'customIcon', default_value='none'),
                        'isKnown': get_attribute_or_default(planet_elem.find('isKnown'), 'value', default_value='false'),
                        'fogColor': get_attribute_or_default(planet_elem.find('fogColor'), 'value', default_value='0,0,0'),
                        'skyColor': get_attribute_or_default(planet_elem.find('skyColor'), 'value', default_value='0,0,0'),
                        'gravitationalMultiplier': get_attribute_or_default(planet_elem.find('gravitationalMultiplier'), 'value', default_value='0'),
                        'orbitalDistance': get_attribute_or_default(planet_elem.find('orbitalDistance'), 'value', default_value='0'),
                        'orbitalTheta': get_attribute_or_default(planet_elem.find('orbitalTheta'), 'value', default_value='0'),
                        'orbitalPhi': get_attribute_or_default(planet_elem.find('orbitalPhi'), 'value', default_value='0'),
                        'retrograde': get_attribute_or_default(planet_elem.find('retrograde'), 'value', default_value='false') == 'true',
                        'avgTemperature': get_attribute_or_default(planet_elem.find('avgTemperature'), 'value', default_value='0'),
                        'rotationalPeriod': get_attribute_or_default(planet_elem.find('rotationalPeriod'), 'value', default_value='0'),
                        'atmosphereDensity': get_attribute_or_default(planet_elem.find('atmosphereDensity'), 'value', default_value='0'),
                        'generateCraters': get_attribute_or_default(planet_elem.find('generateCraters'), 'value', default_value='false') == 'true',
                        'generateCaves': get_attribute_or_default(planet_elem.find('generateCaves'), 'value', default_value='false') == 'true',
                        'generateVolcanos': get_attribute_or_default(planet_elem.find('generateVolcanos'), 'value', default_value='false') == 'true',
                        'generateStructures': get_attribute_or_default(planet_elem.find('generateStructures'), 'value', default_value='false') == 'true',
                        'generateGeodes': get_attribute_or_default(planet_elem.find('generateGeodes'), 'value', default_value='false') == 'true',
                        'biomeIds': get_attribute_or_default(planet_elem.find('biomeIds'), 'value'),
                        'moons': [],
                        }

                    ore_gen_elem = planet_elem.find('.//OreGen')
                    if ore_gen_elem is not None:
                        ore_gen_data = {
                            'ore_block': get_attribute_or_default(ore_gen_elem.find('ore'), 'block'),
                            'minHeight': get_attribute_or_default(ore_gen_elem.find('ore'), 'minHeight', default_value='0'),
                            'maxHeight': get_attribute_or_default(ore_gen_elem.find('ore'), 'maxHeight', default_value='0'),
                            'clumpSize': get_attribute_or_default(ore_gen_elem.find('ore'), 'clumpSize', default_value='0'),
                            'chancePerChunk': get_attribute_or_default(ore_gen_elem.find('ore'), 'chancePerChunk', default_value='0'),
                        }
                        planet_info['oreGen'] = ore_gen_data
    
                    moon_elems = planet_elem.findall('.//planet')
                    for moon_elem in moon_elems:
                        if moon_elem is not None:
                            moon_data = {
                                'name': get_attribute_or_default(moon_elem, 'name'),
                                'DIMID': get_attribute_or_default(moon_elem, 'DIMID', default_value='0'),
                                'customIcon': get_attribute_or_default(moon_elem, 'customIcon'),
                                'isKnown': get_attribute_or_default(moon_elem.find('isKnown'), 'value', default_value='false'),
                                'fogColor': get_attribute_or_default(moon_elem.find('fogColor'), 'value', default_value='0,0,0'),
                                'skyColor': get_attribute_or_default(moon_elem.find('skyColor'), 'value', default_value='0,0,0'),
                                'gravitationalMultiplier': get_attribute_or_default(moon_elem.find('gravitationalMultiplier'), 'value', default_value='0'),
                                'orbitalDistance': get_attribute_or_default(moon_elem.find('orbitalDistance'), 'value', default_value='0'),
                                'orbitalTheta': get_attribute_or_default(moon_elem.find('orbitalTheta'), 'value', default_value='0'),
                                'orbitalPhi': get_attribute_or_default(moon_elem.find('orbitalPhi'), 'value', default_value='0'),
                                'retrograde': get_attribute_or_default(moon_elem.find('retrograde'), 'value', default_value='false') == 'true',
                                'avgTemperature': get_attribute_or_default(moon_elem.find('avgTemperature'), 'value', default_value='0'),
                                'rotationalPeriod': get_attribute_or_default(moon_elem.find('rotationalPeriod'), 'value', default_value='0'),
                                'atmosphereDensity': get_attribute_or_default(moon_elem.find('atmosphereDensity'), 'value', default_value='0'),
                                'generateCraters': get_attribute_or_default(moon_elem.find('generateCraters'), 'value', default_value='false') == 'true',
                                'generateCaves': get_attribute_or_default(moon_elem.find('generateCaves'), 'value', default_value='false') == 'true',
                                'generateVolcanos': get_attribute_or_default(moon_elem.find('generateVolcanos'), 'value', default_value='false') == 'true',
                                'generateStructures': get_attribute_or_default(moon_elem.find('generateStructures'), 'value', default_value='false') == 'true',
                                'generateGeodes': get_attribute_or_default(moon_elem.find('generateGeodes'), 'value', default_value='false') == 'true',
                                'biomeIds': get_attribute_or_default(moon_elem.find('biomeIds'), 'value'),
                                }
                            #print(f"moons: {moon_data}")
                        planet_info['moons'].append(moon_data)
                        

                    star_info['planets'].append(planet_info)

        stars_data.append(star_info)

    return stars_data

if __name__ == "__main__":
    file_path = "PlanetDefs.xml"
    output_folder = 'md_files'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    stars_data = parse_planets_xml(file_path)

    for star in stars_data:
        file_name = os.path.join(output_folder, f'{star['name']}.md')
        current_file_content = []
        current_file_content.append("---")
        current_file_content.append("tags:[Star]")
        current_file_content.append(f"Black Hole: {star['blackHole']}")
        current_file_content.append(f"Number of Gas Giants: {star['numGasGiants']}")
        current_file_content.append(f"Number of Planets: {star['numPlanets']}")
        current_file_content.append(f"Size: {star['size']}")
        current_file_content.append(f"Temperature: {star['temp']}")
        current_file_content.append(f"Coordinates (x, y): ({star['x']}, {star['y']})")
        current_file_content.append("---")
        for planet in star['planets']:
            current_file_content.append(f"Planets:[[{planet['name']}]]")
        create_md_file(file_name, current_file_content)
        
        print(f"Star: {star['name']}")
        print(f"  Black Hole: {star['blackHole']}")
        print(f"  Number of Gas Giants: {star['numGasGiants']}")
        print(f"  Number of Planets: {star['numPlanets']}")
        print(f"  Size: {star['size']}")
        print(f"  Temperature: {star['temp']}")
        print(f"  Coordinates (x, y): ({star['x']}, {star['y']})")
        print("")
        for planet in star['planets']:
            current_file_content.append(f"Planets:[[{planet['name']}]]")

        for planet in star['planets']:
            file_name = os.path.join(output_folder, f'{planet['name']}.md')
            current_file_content = []
            current_file_content.append("---")
            current_file_content.append("tags:[Star]")
            current_file_content.append(f"      DIMID: {planet['DIMID']}")
            current_file_content.append(f"      Custom Icon: {planet['customIcon']}")
            current_file_content.append(f"      Is Known: {planet['isKnown']}")
            current_file_content.append(f"      Fog Color: {planet['fogColor']}")
            current_file_content.append(f"      Sky Color: {planet['skyColor']}")
            current_file_content.append(f"      Gravitational Multiplier: {planet['gravitationalMultiplier']}")
            current_file_content.append(f"      Orbital Distance: {planet['orbitalDistance']}")
            current_file_content.append(f"      Orbital Theta: {planet['orbitalTheta']}")
            current_file_content.append(f"      Orbital Phi: {planet['orbitalPhi']}")
            current_file_content.append(f"      Retrograde: {planet['retrograde']}")
            current_file_content.append(f"      Avg Temperature: {planet['avgTemperature']}")
            current_file_content.append(f"      Rotational Period: {planet['rotationalPeriod']}")
            current_file_content.append(f"      Atmosphere Density: {planet['atmosphereDensity']}")
            current_file_content.append(f"      Generate Craters: {planet['generateCraters']}")
            current_file_content.append(f"      Generate Caves: {planet['generateCaves']}")
            current_file_content.append(f"      Generate Volcanos: {planet['generateVolcanos']}")
            current_file_content.append(f"      Generate Structures: {planet['generateStructures']}")
            current_file_content.append(f"      Generate Geodes: {planet['generateGeodes']}")
            current_file_content.append(f"      Biome IDs: {planet['biomeIds']}")
            current_file_content.append("---")
            create_md_file(file_name, current_file_content)
            
            print(f"    Planet: {planet['name']}")
            print(f"      DIMID: {planet['DIMID']}")
            print(f"      Custom Icon: {planet['customIcon']}")
            print(f"      Is Known: {planet['isKnown']}")
            print(f"      Fog Color: {planet['fogColor']}")
            print(f"      Sky Color: {planet['skyColor']}")
            print(f"      Gravitational Multiplier: {planet['gravitationalMultiplier']}")
            print(f"      Orbital Distance: {planet['orbitalDistance']}")
            print(f"      Orbital Theta: {planet['orbitalTheta']}")
            print(f"      Orbital Phi: {planet['orbitalPhi']}")
            print(f"      Retrograde: {planet['retrograde']}")
            print(f"      Avg Temperature: {planet['avgTemperature']}")
            print(f"      Rotational Period: {planet['rotationalPeriod']}")
            print(f"      Atmosphere Density: {planet['atmosphereDensity']}")
            print(f"      Generate Craters: {planet['generateCraters']}")
            print(f"      Generate Caves: {planet['generateCaves']}")
            print(f"      Generate Volcanos: {planet['generateVolcanos']}")
            print(f"      Generate Structures: {planet['generateStructures']}")
            print(f"      Generate Geodes: {planet['generateGeodes']}")
            print(f"      Biome IDs: {planet['biomeIds']}")

            if 'oreGen' in planet:
                ore_gen = planet['oreGen']
                print(f"      Ore Generation:")
                print(f"        Ore Block: {ore_gen['ore_block']}")
                print(f"        Min Height: {ore_gen['minHeight']}")
                print(f"        Max Height: {ore_gen['maxHeight']}")
                print(f"        Clump Size: {ore_gen['clumpSize']}")
                print(f"        Chance Per Chunk: {ore_gen['chancePerChunk']}")

            print("")
