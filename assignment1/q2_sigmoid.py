#!/usr/bin/env python

import numpy as np


def sigmoid(x):
    """
    Compute the sigmoid function for the input here.

    Arguments:
    x -- A scalar or numpy array.

    Return:
    s -- sigmoid(x)
    """

    ### YOUR CODE HERE
    s = 1/(1 + np.exp(-x))
    ### END YOUR CODE

    return s


def sigmoid_grad(s):
    """
    Compute the gradient for the sigmoid function here. Note that
    for this implementation, the input s should be the sigmoid
    function value of your original input x.

    Arguments:
    s -- A scalar or numpy array.

    Return:
    ds -- Your computed gradient.
    """

    ### YOUR CODE HERE
    ds = s * (1 - s)
    ### END YOUR CODE

    return ds


def test_sigmoid_basic():
    """
    Some simple tests to get you started.
    Warning: these are not exhaustive.
    """
    print "Running basic tests..."
    x = np.array([[1, 2], [-1, -2]])
    f = sigmoid(x)
    g = sigmoid_grad(f)
    print f
    f_ans = np.array([
        [0.73105858, 0.88079708],
        [0.26894142, 0.11920292]])
    assert np.allclose(f, f_ans, rtol=1e-05, atol=1e-06)
    print g
    g_ans = np.array([
        [0.19661193, 0.10499359],
        [0.19661193, 0.10499359]])
    assert np.allclose(g, g_ans, rtol=1e-05, atol=1e-06)
    print "You should verify these results by hand!\n"


def test_sigmoid():
    """
    Use this space to test your sigmoid implementation by running:
        python q2_sigmoid.py
    This function will not be called by the autograder, nor will
    your tests be graded.
    """
    print "Running your tests..."
    ### YOUR CODE HERE

    print "Test case 1: scalar"
    x = -0.99
    f = sigmoid(x)
    g = sigmoid_grad(f)
    print f
    f_ans = 0.270912078
    assert np.allclose(f, f_ans, rtol=1e-05, atol=1e-06)
    print g
    g_ans = 0.197518724
    assert np.allclose(g, g_ans, rtol=1e-05, atol=1e-06)
    print "Test case 1: passed\n\n"

    print "Test case 2: 1-d array with minor value"
    x = np.array([4.1, -5.0])
    f = sigmoid(x)
    g = sigmoid_grad(f)
    print f
    f_ans = np.array([0.98369750, 0.00669285])
    assert np.allclose(f, f_ans, rtol=1e-05, atol=1e-06)
    print g
    g_ans = np.array([0.01603673, 0.00664806])
    assert np.allclose(g, g_ans, rtol=1e-05, atol=1e-06)
    print "Test case 2: passed\n\n"

    print "Test case 3: AxB matrix, where dim A > dim B"
    x = np.array([[10, 1, -0.1],
                  [4.1, -5.0, 2],
                  [-1, -1, 1]])
    f = sigmoid(x)
    g = sigmoid_grad(f)
    print f
    f_ans = np.array([[0.99995460, 0.73105858, 0.47502081],
                      [0.98369750, 0.00669285, 0.88079708],
                      [0.26894142, 0.26894142, 0.73105858]])
    assert np.allclose(f, f_ans, rtol=1e-05, atol=1e-06)
    print g
    g_ans = np.array([[4.53958077e-05, 0.19661193, 0.24937604],
                      [0.01603673, 0.00664806, 0.10499359],
                      [0.19661193, 0.19661193, 0.19661193]])
    assert np.allclose(g, g_ans, rtol=1e-05, atol=1e-06)
    print "Test case 3: passed\n\n"
    ### END YOUR CODE

    print "All test cases passed."


if __name__ == "__main__":
    test_sigmoid_basic();
    test_sigmoid()
