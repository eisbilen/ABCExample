from abc import ABCMeta, abstractmethod

import pandas as pd

class AbstactClassExample(metaclass = ABCMeta):

    def __init__(self, title, first_name, surname):
        self._title = title
        self._first_name = first_name
        self._surname = surname

    @abstractmethod
    def display_name(self):
        pass

    @property
    @abstractmethod
    def first_name(self):
        pass

    @first_name.setter
    @abstractmethod
    def first_name(self):
        pass

class EmployeeName(AbstactClassExample):

    def display_name(self):
        print(self._title + " " + self._first_name + " " + self._surname)
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        self._first_name = value

name = EmployeeName("Mr", "Erdem", "Isbilen")
name.display_name()

name.first_name = "EFE"
name.display_name()





class AbstactClassCSV(metaclass = ABCMeta):

    def __init__(self, path, file_name):
        self._path = path
        self._file_name = file_name

    @property
    @abstractmethod
    def path(self):
        pass

    @path.setter
    @abstractmethod
    def path(self,value):
        pass

    @property
    @abstractmethod
    def file_name(self):
        pass

    @file_name.setter
    @abstractmethod
    def file_name(self,value):
        pass

    @abstractmethod
    def display_summary(self):
        pass



class CSVGetInfo(AbstactClassCSV):
    """ This class displays the summary of the tabular data contained in a CSV file """

    @property
    def path(self):
        """ The docstring for the path property """
        print("Getting value of path")
        return self._path

    @path.setter
    def path(self,value):
        if '/' in value:  
            self._path = value
            print("Setting value of path to {}".format(value))
        else:
            print("Error: {} is not a valid path string".format(value))

    @property
    def file_name(self):
        """ The docstring for the file_name property """
        print("Getting value of file_name")
        return self._file_name

    @file_name.setter
    def file_name(self,value):
        if '.' in value:  
            self._file_name = value
            print("Setting value of file_name to {}".format(value))
        else:
            print("Error: {} is not a valid file name".format(value))

    def display_summary(self):
        data = pd.read_csv(self._path + self._file_name)
        print(self._file_name)
        print(data.info())

if __name__ == '__main__':

    
    data_by_genres = CSVGetInfo("/Users/erdemisbilen/Lessons/", "data_by_genres.csv")
    data_by_artists = CSVGetInfo("/Users/erdemisbilen/Lessons/", "data_by_artists.csv")

    data_by_genres.display_summary()
    data_by_artists.display_summary()

    print(data_by_artists.__dict__)
    print(data_by_artists.__class__)
    print(data_by_artists.__dir__)

    print(data_by_genres.__dict__)
    print(data_by_genres.__class__)
    print(data_by_genres.__dir__)

    abc_instantiation = AbstactClassCSV("/Users/erdemisbilen/Lessons/", "data_by_genres.csv")

   



