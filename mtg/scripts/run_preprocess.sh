EXPANSION=FDN

DATA_DIR=~/"General/Learning/Cloning/mtg/Data/"
GAME_DATA_FILE_PREFIX="game_data_public."
DRAFT_DATA_FILE_PREFIX="draft_data_public."
DATA_FILE_SUFFIX=".PremierDraft.csv"

GAME_DATA_PATH="${DATA_DIR}${GAME_DATA_FILE_PREFIX}${EXPANSION}${DATA_FILE_SUFFIX}"
DRAFT_DATA_PATH="${DATA_DIR}${DRAFT_DATA_FILE_PREFIX}${EXPANSION}${DATA_FILE_SUFFIX}"
EXPANSION_PATH="${DATA_DIR}ExpansionData/${EXPANSION}.pkl"

python preprocess.py  --expansion $EXPANSION \
                          --game_data $GAME_DATA_PATH \
                          --draft_data $DRAFT_DATA_PATH \
                          --expansion_fname $EXPANSION_PATH