import caffe


def save_model(MainModel, network_filepath, weight_filepath, dump_filepath):
    dump_net = dump_filepath + '.prototxt'
    dump_weight = dump_filepath + '.caffemodel'
    MainModel.make_net(dump_net)
    MainModel.gen_weight(weight_filepath, dump_weight, dump_net)
    model = caffe.Net(dump_net, dump_weight, caffe.TEST)
    print('Caffe model files are saved as [{}] and [{}], generated by [{}.py] and [{}].'.format(
        dump_net, dump_weight, network_filepath, weight_filepath))
