from typing import Type

from projects.models import DOCUMENT_CLASSIFICATION, SEQUENCE_LABELING, SEQ2SEQ, SPEECH2TEXT, IMAGE_CLASSIFICATION, \
    INTENT_DETECTION_AND_SLOT_FILLING
from . import catalog, repositories, writers


def create_repository(project) -> repositories.BaseRepository:
    mapping = {
        DOCUMENT_CLASSIFICATION: repositories.TextClassificationRepository,
        SEQUENCE_LABELING: repositories.SequenceLabelingRepository,
        SEQ2SEQ: repositories.Seq2seqRepository,
        IMAGE_CLASSIFICATION: repositories.FileRepository,
        SPEECH2TEXT: repositories.Speech2TextRepository,
        INTENT_DETECTION_AND_SLOT_FILLING: repositories.IntentDetectionSlotFillingRepository,
    }
    if project.project_type not in mapping:
        ValueError(f'Invalid project type: {project.project_type}')
    repository = mapping.get(project.project_type)(project)
    return repository


def create_writer(file_format: str) -> Type[writers.BaseWriter]:
    mapping = {
        catalog.CSV.name: writers.CsvWriter,
        catalog.JSON.name: writers.JSONWriter,
        catalog.JSONL.name: writers.JSONLWriter,
        catalog.FastText.name: writers.FastTextWriter,
        catalog.IntentAndSlot.name: writers.IntentAndSlotWriter
    }
    if file_format not in mapping:
        ValueError(f'Invalid format: {file_format}')
    return mapping[file_format]
