import numpy as np


def softmax(x):
    """Compute the softmax function for each row of the input x.

    It is crucial that this function is optimized for speed because
    it will be used frequently in later code. You might find numpy
    functions np.exp, np.sum, np.reshape, np.max, and numpy
    broadcasting useful for this task.

    Numpy broadcasting documentation:
    http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html

    You should also make sure that your code works for a single
    D-dimensional vector (treat the vector as a single row) and
    for N x D matrices. This may be useful for testing later. Also,
    make sure that the dimensions of the output match the input.

    You must implement the optimization in problem 1(a) of the
    written assignment!

    Arguments:
    x -- A D dimensional vector or N x D dimensional numpy matrix.

    Return:
    x -- You are allowed to modify x in-place
    """
    orig_shape = x.shape

    if len(x.shape) > 1:
        # Matrix
        ### YOUR CODE HERE
        m = np.max(x, axis=1, keepdims = True)
        x = x - m
        x = np.exp(x)
        s = np.sum(x, axis=1, keepdims = True)
        x = x/s
        ### END YOUR CODE
    else:
        # Vector
        ### YOUR CODE HERE
        m = np.max(x)
        x = x - m
        x = np.exp(x)
        s = np.sum(x)
        x = x/s
        ### END YOUR CODE

    assert x.shape == orig_shape
    return x


def test_softmax_basic():
    """
    Some simple tests to get you started.
    Warning: these are not exhaustive.
    """
    print "Running basic tests..."
    test1 = softmax(np.array([1,2]))
    print test1
    ans1 = np.array([0.26894142,  0.73105858])
    assert np.allclose(test1, ans1, rtol=1e-05, atol=1e-06)

    test2 = softmax(np.array([[1001,1002],[3,4]]))
    print test2
    ans2 = np.array([
        [0.26894142, 0.73105858],
        [0.26894142, 0.73105858]])
    assert np.allclose(test2, ans2, rtol=1e-05, atol=1e-06)

    test3 = softmax(np.array([[-1001,-1002]]))
    print test3
    ans3 = np.array([0.73105858, 0.26894142])
    assert np.allclose(test3, ans3, rtol=1e-05, atol=1e-06)

    print "You should be able to verify these results by hand!\n"


def test_softmax():
    """
    Use this space to test your softmax implementation by running:
        python q1_softmax.py
    This function will not be called by the autograder, nor will
    your tests be graded.
    """
    print "Running your tests..."

    # Test scenario: N x D dimension, when N > D
    test4 = softmax(np.array([[1001,1002],[3,4], [100, 200]]))
    print test4
    ans4 = np.array([
        [0.26894142, 0.73105858],
        [0.26894142, 0.73105858],
        [0, 1]])
    assert np.allclose(test4, ans4, rtol=1e-05, atol=1e-06)

    # Test scenario: N x D dimension, when N < D
    test5 = softmax(np.array([[1001,1002,1005,1007],[3,1,2,4]]))
    print test5
    ans5 = np.array([
        [0.0021657 ,  0.00588697,  0.11824302,  0.87370431],
        [0.23688282,  0.0320586 ,  0.08714432,  0.64391426]])
    assert np.allclose(test5, ans5, rtol=1e-05, atol=1e-06)


if __name__ == "__main__":
    test_softmax_basic()
    test_softmax()
