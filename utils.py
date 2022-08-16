from candidate import Candidate
import json


def load_candidates_from_json(path):
    """Возвращает список всех кадидатов"""
    list_of_candidates = []

    with open(path, "r", encoding="utf-8", ) as file:
        data = json.load(file)

    for i in data:
        person = Candidate(i["id"], i["name"], i["picture"], i["position"], i["gender"], i["age"], i["skills"])
        list_of_candidates.append(person)

    return list_of_candidates


def get_candidate(candidate_id, list_of_candidates):
    """Возвращает кандидата по его ID"""
    for item in list_of_candidates:
        if item.id == candidate_id:
            return item


def get_candidates_by_name(candidate_name, list_of_candidates):
    """Возвращает кандидатов по имени"""
    candidates_by_names = []
    for item in list_of_candidates:
        if candidate_name.lower() in item.name.lower():
            candidates_by_names.append(item)
    return candidates_by_names

def get_candidates_by_skill(skill_name, list_of_candidates):
    """Возвращает кандидатов по навыкам"""
    candidates_by_skills = []
    for item in list_of_candidates:
        if skill_name.lower() in item.skills.lower():
            candidates_by_skills.append(item)
    return candidates_by_skills