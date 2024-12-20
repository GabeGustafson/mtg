import argparse
from mtg.obj.expansion import get_expansion_obj_from_name
import pickle
import os


def main():
    # check expansion filepath ahead of time
    if not os.path.exists(FLAGS.expansion_fname):
        print("Error: Expansion file does not exist:", FLAGS.expansion_fname)
        return
        
    EXPANSION = get_expansion_obj_from_name(FLAGS.expansion)
    expansion = EXPANSION(bo1=FLAGS.game_data, draft=FLAGS.draft_data, ml_data=True)
    with open(FLAGS.expansion_fname, "wb") as f:
        pickle.dump(expansion, f)

    print("\nExpansion data stored in:", FLAGS.expansion_fname)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--expansion",
        type=str,
        default="VOW",
        help="name of magic expansion corresponding to data files",
    )
    parser.add_argument(
        "--game_data", type=str, default=None, help="path to bo1 game data"
    )
    parser.add_argument(
        "--draft_data", type=str, default=None, help="path to bo1 draft data"
    )
    parser.add_argument(
        "--expansion_fname",
        type=str,
        default="expansion.pkl",
        help="path/to/fname.pkl for where we should store the expansion object",
    )
    FLAGS, unparsed = parser.parse_known_args()
    main()
