import glob,os
import pandas as pd

class fileClass:
    data_folder = "C:/Users/ashis/Desktop/hatchway_backend/csvdata/"
    file_name =  ["C:/Users/ashis/Desktop/hatchway_backend/csvdata/empdata.csv","C:/Users/ashis/Desktop/hatchway_backend/csvdata/highscore.csv"]
    def read_file(self):
        files = map(lambda x: os.path.join(self.data_folder, x), os.listdir(self.data_folder))
        for i in self.file_name:
            if i in files:
                try:
                    if i == "C:/Users/ashis/Desktop/hatchway_backend/csvdata/empdata.csv":
                        df = pd.read_csv(i, parse_dates=['Hire Date'])
                        print('Max Salary of Employee', df['Salary'].max())
                        print('Min Salary of Employee', df['Salary'].max())
                       
                    if i == "C:/Users/ashis/Desktop/hatchway_backend/csvdata/highscore.csv":
                        df = pd.read_csv(i,index_col=None,header=0, na_values="NaN")
                        print('Max HighScore', df['Highscore'].max())
                        
                except Exception as e:
                    print ("Error in reading", self.file_name)
                    print (e)
                    df = pd.DataFrame()

            else:
                print ("File Not Found.")
                df = pd.DataFrame()
            

     
# your code goes here
def main():
    file1 = fileClass()
    print(file1.read_file())
    
if __name__ == '__main__':
    main()
