from __future__ import print_function, absolute_import, division
from collections import namedtuple


#--------------------------------------------------------------------------------
# Definitions
#--------------------------------------------------------------------------------

# a label and all meta information
Label = namedtuple( 'Label' , [

    'name'        , # The identifier of this label, e.g. 'car', 'person', ... .
                    # We use them to uniquely name a class

    'id'          , # An integer ID that is associated with this label.
                    # The IDs are used to represent the label in ground truth images
                    # An ID of -1 means that this label does not have an ID and thus
                    # is ignored when creating ground truth images (e.g. license plate).
                    # Do not modify these IDs, since exactly these IDs are expected by the
                    # evaluation server.

    'trainId'     , # Feel free to modify these IDs as suitable for your method. Then create
                    # ground truth images with train IDs, using the tools provided in the
                    # 'preparation' folder. However, make sure to validate or submit results
                    # to our evaluation server using the regular IDs above!
                    # For trainIds, multiple labels might have the same ID. Then, these labels
                    # are mapped to the same class in the ground truth images. For the inverse
                    # mapping, we use the label that is defined first in the list below.
                    # For example, mapping all void-type classes to the same ID in training,
                    # might make sense for some approaches.
                    # Max value is 255!

    'category'    , # The name of the category that this label belongs to

    'categoryId'  , # The ID of this category. Used to create ground truth images
                    # on category level.

    'hasInstances', # Whether this label distinguishes between single instances or not

    'ignoreInEval', # Whether pixels having this class as ground truth label are ignored
                    # during evaluations or not

    'color'       , # The color of this label
    ] )


#--------------------------------------------------------------------------------
# A list of all labels
#--------------------------------------------------------------------------------

# Please adapt the train IDs as appropriate for your approach.
# Note that you might want to ignore labels with ID 255 during training.
# Further note that the current train IDs are only a suggestion. You can use whatever you like.
# Make sure to provide your results using the original IDs and not the training IDs.
# Note that many IDs are ignored in evaluation and thus you never need to predict these!


labels = [
    #      name         id  trainId category catId hasInstances ignoreInEval color
    Label( 'void'    ,  0,    0,  'void',      0,  False,  False,  ( 0, 0, 0)),
    
    Label( 's_w_d'   ,  200,  1,  'dividing',  1,  False,  False,  ( 70, 130, 180)),
    Label( 's_y_d'   ,  204,  1,  'dividing',  1,  False,  False,  (220, 20, 60)),
    Label( 'ds_w_dn' ,  213,  1,  'dividing',  1,  False,  True,  (128, 0, 128)),
    Label( 'ds_y_dn' ,  209,  1,  'dividing',  1,  False,  False,  (255, 0, 0)),
    Label( 'sb_w_do' ,  206,  1,  'dividing',  1,  False,  True,  ( 0, 0, 60)),
    Label( 'sb_y_do' ,  207,  1,  'dividing',  1,  False,  True,  ( 0, 60, 100)),
    
    Label( 'b_w_g'   ,  201,  2,  'guiding',   2,  False,  False,  ( 0, 0, 142)),
    Label( 'b_y_g'   ,  203,  2,  'guiding',   2,  False,  False,  (119, 11, 32)),
    Label( 'db_w_g'  ,  211,  2,  'guiding',   2,  False,  True,  (244, 35, 232)),
    Label( 'db_y_g'  ,  208,  2,  'guiding',   2,  False,  True,  ( 0, 0, 160)),
    
    Label( 'db_w_s'  ,  216,  3,  'stopping',  3,  False,  True,  (153, 153, 153)),
    Label( 's_w_s'   ,  217,  3,  'stopping',  3,  False,  False,  (220, 220, 0)),
    Label( 'ds_w_s'  ,  215,  3,  'stopping',  3,  False,  True,  (250, 170, 30)),
    
    # V 形线条、V 形图案或箭头交通标志表示左方或右方有急转弯
    Label( 's_w_c'   ,  218,  4,  'chevron',   4,  False,  True,  (102, 102, 156)),
    Label( 's_y_c'   ,  219,  4,  'chevron',   4,  False,  True,  (128, 0, 0)),
    
    Label( 's_w_p'   ,  210,  5,  'parking',   5,  False,  False,  (128, 64, 128)),
    Label( 's_n_p'   ,  232,  5,  'parking',   5,  False,  True,   (238, 232, 170)),
    
    Label( 'c_wy_z'  ,  214,  6,  'zebra',     6,  False,  False,  (190, 153, 153)),
    
    Label( 'a_w_u'   ,  202,  7,  'thru/turn',  7,  False,  True,   (0, 0, 230)),
    Label( 'a_w_t'   ,  220,  7,  'thru/turn',  7,  False,  False,  (128, 128, 0)),
    Label( 'a_w_tl'  ,  221,  7,  'thru/turn',  7,  False,  False,  (128, 78, 160)),
    Label( 'a_w_tr'  ,  222,  7,  'thru/turn',  7,  False,  False,  (150, 100, 100)),
    Label( 'a_w_tlr' ,  231,  7,  'thru/turn',  7,  False,  True,   (255, 165, 0)),
    Label( 'a_w_l'   ,  224,  7,  'thru/turn',  7,  False,  False,  (180, 165, 180)),
    Label( 'a_w_r'   ,  225,  7,  'thru/turn',  7,  False,  False,  (107, 142, 35)),
    Label( 'a_w_lr'  ,  226,  7,  'thru/turn',  7,  False,  False,  (201, 255, 229)),
    Label( 'a_n_lu'  ,  230,  7,  'thru/turn',  7,  False,  True,  (0, 191, 255)),
    Label( 'a_w_tu'  ,  228,  7,  'thru/turn',  7,  False,  True,  ( 51, 255, 51)),
    Label( 'a_w_m'   ,  229,  7,  'thru/turn',  7,  False,  True,  (250, 128, 114)),
    Label( 'a_y_t'   ,  233,  7,  'thru/turn',  7,  False,  True,  (127, 255, 0)),
    
    Label( 'b_n_sr'  ,  205,  8,  'reduction',  8,  False,  False,  (255, 128, 0)),
    Label( 'd_wy_za' ,  212,  8,  'attention',  8,  False,  True,  ( 0, 255, 255)),
    Label( 'r_wy_np' ,  227,  8,  'no parking', 8,  False,  False,  (178, 132, 190)),
    Label( 'vom_wy_n',  223,  8,  'others',     8,  False,  True,  (128, 128, 64)),
    Label( 'om_n_n'  ,  250,  8,  'others',     8,  False,  False,  (102, 0, 204)),
    
    Label( 'noise'   ,  249,  0,  'ignored',  0,  False,  True,  ( 0, 153, 153)),
    Label( 'ignored' ,  255,  0,  'ignored',  0,  False,  True,  (255, 255, 255)),
]



#--------------------------------------------------------------------------------
# Create dictionaries for a fast lookup
#--------------------------------------------------------------------------------

# Please refer to the main method below for example usages!

# name to label object
name2label      = { label.name    : label for label in labels           }
# id to label object
id2label        = { label.id      : label for label in labels           }
# trainId to label object
trainId2label   = { label.trainId : label for label in reversed(labels) }
# category to list of label objects
category2labels = {}
for label in labels:
    category = label.category
    if category in category2labels:
        category2labels[category].append(label)
    else:
        category2labels[category] = [label]

#--------------------------------------------------------------------------------
# Assure single instance name
#--------------------------------------------------------------------------------

# returns the label name that describes a single instance (if possible)
# e.g.     input     |   output
#        ----------------------
#          car       |   car
#          cargroup  |   car
#          foo       |   None
#          foogroup  |   None
#          skygroup  |   None
def assureSingleInstanceName( name ):
    # if the name is known, it is not a group
    if name in name2label:
        return name
    # test if the name actually denotes a group
    if not name.endswith("group"):
        return None
    # remove group
    name = name[:-len("group")]
    # test if the new name exists
    if not name in name2label:
        return None
    # test if the new name denotes a label that actually has instances
    if not name2label[name].hasInstances:
        return None
    # all good then
    return name



def get_color_to_label(labels, type_filter=None, with_ignored=True):
    assert type_filter is None or isinstance(type_filter, list), "check type_filter"
    color_to_label = {}

    for item in labels:
        if type_filter is not None and item.categoryId not in type_filter:
            continue
        c = item.color[::-1]
        color_to_label[c] = {'name': item.name, 'id': item.id, 'trainId': item.trainId, 'catId':item.categoryId}
    
    if with_ignored:
        color_to_label[(255, 255, 255)] = {'name': 'void', 'id': 255, 'trainId': 0, 'catId': 0}
    
    return color_to_label




#--------------------------------------------------------------------------------
# Main for testing
#--------------------------------------------------------------------------------

# just a dummy main
if __name__ == "__main__":
    # Print all the labels
    print("List of cityscapes labels:")
    print("")
    print("    {:>21} | {:>3} | {:>7} | {:>14} | {:>10} | {:>12} | {:>12}".format( 'name', 'id', 'trainId', 'category', 'categoryId', 'hasInstances', 'ignoreInEval' ))
    print("    " + ('-' * 98))
    for label in labels:
        print("    {:>21} | {:>3} | {:>7} | {:>14} | {:>10} | {:>12} | {:>12}".format( label.name, label.id, label.trainId, label.category, label.categoryId, label.hasInstances, label.ignoreInEval ))
    print("")

    print("Example usages:")

    # Map from name to label
    name = 'a_w_t'
    id   = name2label[name].id
    print("ID of label '{name}': {id}".format( name=name, id=id ))

    # Map from ID to label
    category = id2label[id].category
    print("Category of label with ID '{id}': {category}".format( id=id, category=category ))

    # Map from trainID to label
    trainId = 0
    name = trainId2label[trainId].name
    print("Name of label with trainID '{id}': {name}".format( id=trainId, name=name ))

