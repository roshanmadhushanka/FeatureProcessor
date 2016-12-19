from featureeng import Frame
from featureeng.presenting import Chart
from featureeng.parser import XMLParser





data_frame = Frame('test.csv')
XMLParser.apply_feature_eng(frame=data_frame, xml_file='flow')

data_frame.display()