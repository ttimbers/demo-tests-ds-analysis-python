import pandas as pd
import pytest
import sys
import os

# Import the count_classes function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.count_classes import count_classes

# Test data
five_classes_3_obs = pd.DataFrame({'class_labels': ['class1', 'class2', 'class3', 'class4', 'class5'] * 3})
two_classes_3_obs = pd.DataFrame({'class_labels': ['class1', 'class2'] * 3})
one_class_3_obs = pd.DataFrame({'class_labels': ['class1'] * 3})
empty_df = pd.DataFrame({'class_labels': []})
#vector_class_labels = ['class1', 'class2'] * 3
two_classes_3_obs_as_list = [{'class_labels': ['class1', 'class2'] * 3}]

# Expected outputs
five_classes_3_obs_output = pd.DataFrame({'class': ['class1', 'class2', 'class3', 'class4', 'class5'],
                                          'count': [3, 3, 3, 3, 3]})
two_classes_3_obs_output = pd.DataFrame({'class': ['class1', 'class2'],
                                'count': [3, 3]})
one_class_3_obs_output = pd.DataFrame({'class': ['class1'],
                              'count': [3]})
empty_df_output = pd.DataFrame({'class': [],
                              'count': []})

# Test for correct return type
def test_count_classes_returns_dataframe():
    result = count_classes(two_classes_3_obs, 'class_labels')
    assert isinstance(result, pd.DataFrame), "count_classes` should return a pandas data frame"

# Test for correct number of unique classes in the column passed to `class_col`
def test_count_classes_number_of_rows():
    assert count_classes(five_classes_3_obs, 'class_labels').shape[0] == five_classes_3_obs_output.shape[0]
    assert count_classes(two_classes_3_obs, 'class_labels').shape[0] == two_classes_3_obs_output.shape[0]
    assert count_classes(one_class_3_obs, 'class_labels').shape[0] == one_class_3_obs_output.shape[0]
    assert count_classes(empty_df, 'class_labels').shape[0] == empty_df_output.shape[0]

# Test for correct values in the data frame
def test_count_classes_count_values():
    pd.testing.assert_frame_equal(count_classes(five_classes_3_obs, 'class_labels'), five_classes_3_obs_output)
    pd.testing.assert_frame_equal(count_classes(two_classes_3_obs, 'class_labels'), two_classes_3_obs_output)
    pd.testing.assert_frame_equal(count_classes(one_class_3_obs, 'class_labels'), one_class_3_obs_output)

# Test for correct error handling for incorrect type of column value 
# (not a string)
def test_count_classes_type_error():
    with pytest.raises(KeyError):
        count_classes(two_classes_3_obs, 1)

# Test for correct error handling for incorrect object type 
# (not a pandas data frame)
def test_count_classes_attribute_error():
    with pytest.raises(AttributeError):
        count_classes(two_classes_3_obs_as_list, 'class1')
