import argparse
import os
import glob
import matplotlib.pyplot as plt
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description = "This script parses amber mdout files to extract the total energy.")
    parser.add_argument("path", help = "The filepath for the file to analyze.")
    parser.add_argument("-make_plots", help="Flag to create plots", action='store_true')
    args = parser.parse_args()
    print(args.path)
    filenames = glob.glob(args.path)
    make_plots = args.make_plots

    for filename in filenames:
        energies =[]
        fname = os.path.basename(filename).split('.')[0]
        
        with open(filename,"r") as dataset:
            for line in dataset:
                if 'Etot' in line:
                    words = line.split()
                    energies.append(words[2])
        values = energies[:-2]
        outfile_name = F'{fname}_Etot.txt'

        with open(outfile_name, 'w+') as newfile:
            for value in values:
                newfile.write(F'{value} \n')
        if make_plots == True:
            plt.figure()
            plt.plot(values)
            plt.savefig(F'{fname}.png')
