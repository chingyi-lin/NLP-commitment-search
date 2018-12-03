def train_test_split_common(X, Y, test_size=0.2, random_state=0):
  from sklearn.model_selection import train_test_split
  train_x, test_x, train_y, test_y=train_test_split(X, Y, test_size=test_size, random_state=random_state)
  return train_x, test_x, train_y, test_y