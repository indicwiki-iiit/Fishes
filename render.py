import pandas as pd
from jinja2 import Environment, FileSystemLoader
from genXML import hiwiki, writePage

def getData(datarow):
    data = {
            'ID': datarow[0],
            'binomialName_eng': datarow[1],
            'binomialName': datarow[2],
            'species_eng': datarow[3],
            'Species_hi': datarow[4],
            #'Common Name': datarow[5],
            'commonName': datarow[6],
            #'Authors': datarow[7],
            'authors_1': datarow[8],
            'year': datarow[9],
            'genus_eng': datarow[10],
            'genus': datarow[11],
            #'Subfamily': datarow[12],
            'subfamily': datarow[13],
            #'Family': datarow[14],
            'family': datarow[15],
            #'Order': datarow[16],
            'order': datarow[17],
            #'Class': datarow[18],
            'class': datarow[19],
            'Phylum': datarow[20],
            'Phylum_hi': datarow[21],
            'Kingdom': datarow[22],
            'Kingdom_hi': datarow[23],
            #'Environment': datarow[24],
            'environment': datarow[25],
            #'Habitat': datarow[26],
            'habitat': datarow[27],
            #'habitat_defn': datarow[28],
            'habitatDefn': datarow[29],
            #'Migration': datarow[30],
            'migration': datarow[31],
            #'mig_defn': datarow[32],
            'migrationDefn': datarow[33],
            #'IUCN Status': datarow[34],
            'status': datarow[35],
            #'status_defn': datarow[36],
            'statusDefn': datarow[37],
            #'Threat Level': datarow[38],
            'threat': datarow[39],
            #'Climate': datarow[40],
            'climate': datarow[41],
            #'Area': datarow[42],
            'area': datarow[43],
            'maxLen': datarow[44],
            #'Max Weight': datarow[45],
            'maxWeight': datarow[46],
            'maxAge': datarow[47],
            'depthRange': datarow[48],
            'pH': datarow[49],
            'dH': datarow[50],
            #'Mode of Reproduction': datarow[51],
            'reproduction': datarow[52],
            #'reproduction_defn': datarow[53],
            'reproductionDefn': datarow[54],
            #'Fertilization': datarow[55],
            'fertilization': datarow[56],
            #'fertilization_defns': datarow[57],
            'fertilizationDefn': datarow[58],
            #'fisheries': datarow[59],
            'fisheries': datarow[60],
            #'aquarium': datarow[61],
            'aquarium': datarow[62],
            #'gamefish': datarow[63],
            'gamefish': datarow[64],
            #'bait': datarow[65],
            'bait': datarow[66],
            'mainRef': datarow[67],
            'img': datarow[68],
            'statusRef': datarow[69],
            'IUCN link': datarow[70],
            'migRef': datarow[71],
            'climateRef': datarow[72],
            'depthRef': datarow[73],
            'lastRef': datarow[74],
            'habitat_ref': datarow[75],
            'wikidata': datarow[76],
            #'Author': datarow[77],
            #'Author Link': datarow[78],
            #'categories': datarow[79],
            'categories': datarow[80],
            'authors_2': datarow[81],
            'checkDepth': datarow[82]
    }
    return data


def main():
    fileLoader = FileSystemLoader('./')
    env = Environment(loader=fileLoader)
    template = env.get_template('template.j2')
    df = pd.read_pickle('FinalFishesHindi.pkl')
    df = df.fillna('')

    xmlDump = open('FinalFishesDump.xml', "w", encoding="utf-8")
    xmlDump.write(hiwiki+'\n')

    initial_page_id = 2600000
    
    for i in range(len(df)):
        print(i)
        row = df.iloc[i]
        text = template.render(getData(row))
        title = df.loc[i, 'Binomial Name_hi']
        writePage(initial_page_id, title, text, xmlDump)
        initial_page_id += 1

    xmlDump.write('</mediawiki>')
    xmlDump.close()


if __name__ == '__main__':
    main()