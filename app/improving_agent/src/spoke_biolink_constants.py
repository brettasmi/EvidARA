from collections import defaultdict
# internal
BIOLINK_ASSOCIATION_TYPE = 'biolink_association_type'
RELATIONSHIP_ONTOLOGY_CURIE = 'relationship_ontology_curie'

# Nodes
BIOLINK_ENTITY_BIOLOGICAL_PROCESS = 'biolink:BiologicalProcess'
BIOLINK_ENTITY_CELL = 'biolink:Cell'
BIOLINK_ENTITY_CELLULAR_COMPONENT = 'biolink:CellularComponent'
BIOLINK_ENTITY_CHEMICAL_SUBSTANCE = 'biolink:ChemicalSubstance'
BIOLINK_ENTITY_DRUG = 'biolink:Drug'
BIOLINK_ENTITY_DISEASE = 'biolink:Disease'
BIOLINK_ENTITY_FOOD = 'biolink:Food'
BIOLINK_ENTITY_GENE = 'biolink:Gene'
BIOLINK_ENTITY_GROSS_ANATOMICAL_STRUCTURE = 'biolink:GrossAnatomicalStructure'
BIOLINK_ENTITY_MOLECULAR_ACTIVITY = 'biolink:MolecularActivity'
BIOLINK_ENTITY_NAMED_THING = 'biolink:NamedThing'
BIOLINK_ENTITY_NUTRIENT = 'biolink:Nutrient'
BIOLINK_ENTITY_ORGANISM_TAXON = 'biolink:OrganismTaxon'
BIOLINK_ENTITY_PATHWAY = 'biolink:Pathway'
BIOLINK_ENTITY_PHENOTYPIC_FEATURE = 'biolink:PhenotypicFeature'
BIOLINK_ENTITY_PROTEIN = 'biolink:Protein'

SPOKE_LABEL_ANATOMY = 'Anatomy'
SPOKE_LABEL_ANATOMY_CELL_TYPE = 'AnatomyCellType'
SPOKE_LABEL_BIOLOGICAL_PROCESS = 'BiologicalProcess'
SPOKE_LABEL_CELL_TYPE = 'CellType'
SPOKE_LABEL_CELLULAR_COMPONENT = 'CellularComponent'
SPOKE_LABEL_COMPOUND = 'Compound'
SPOKE_LABEL_DISEASE = 'Disease'
SPOKE_LABEL_EC = 'EC'
SPOKE_LABEL_FOOD = 'Food'
SPOKE_LABEL_GENE = 'Gene'
SPOKE_LABEL_MOLECULAR_FUNCTION = 'MolecularFunction'
SPOKE_LABEL_NUTRIENT = 'Nutrient'
SPOKE_LABEL_ORGANISM = 'Organism'
SPOKE_LABEL_PATHWAY = 'Pathway'
SPOKE_LABEL_PHARMACOLOGIC_CLASS = 'PharmacologicClass'
SPOKE_LABEL_PROTEIN = 'Protein'
SPOKE_LABEL_REACTION = 'Reaction'
SPOKE_LABEL_SARSCOV2 = 'SARSCov2'
SPOKE_LABEL_SIDE_EFFECT = 'SideEffect'
SPOKE_LABEL_SYMPTOM = 'Symptom'

SPOKE_ANY_TYPE = '*'

BIOLINK_SPOKE_NODE_MAPPINGS = {
    BIOLINK_ENTITY_BIOLOGICAL_PROCESS: SPOKE_LABEL_BIOLOGICAL_PROCESS,
    BIOLINK_ENTITY_CELL: SPOKE_LABEL_CELL_TYPE,
    BIOLINK_ENTITY_CELLULAR_COMPONENT: SPOKE_LABEL_CELLULAR_COMPONENT,
    BIOLINK_ENTITY_CHEMICAL_SUBSTANCE: SPOKE_LABEL_COMPOUND,
    BIOLINK_ENTITY_DISEASE: SPOKE_LABEL_DISEASE,
    BIOLINK_ENTITY_DRUG: SPOKE_LABEL_COMPOUND,
    BIOLINK_ENTITY_FOOD: SPOKE_LABEL_FOOD,
    BIOLINK_ENTITY_GENE: SPOKE_LABEL_GENE,
    BIOLINK_ENTITY_GROSS_ANATOMICAL_STRUCTURE: SPOKE_LABEL_ANATOMY,
    BIOLINK_ENTITY_MOLECULAR_ACTIVITY: [SPOKE_LABEL_EC, SPOKE_LABEL_MOLECULAR_FUNCTION, SPOKE_LABEL_REACTION],
    BIOLINK_ENTITY_NUTRIENT: SPOKE_LABEL_NUTRIENT,
    BIOLINK_ENTITY_ORGANISM_TAXON: SPOKE_LABEL_ORGANISM,
    BIOLINK_ENTITY_PATHWAY: SPOKE_LABEL_PATHWAY,
    BIOLINK_ENTITY_PHENOTYPIC_FEATURE: SPOKE_LABEL_SYMPTOM,
    BIOLINK_ENTITY_PROTEIN: [SPOKE_LABEL_PROTEIN, SPOKE_LABEL_SARSCOV2],
    # We give this a special value instead of leaving it null for filter
    # clause construction later on
    BIOLINK_ENTITY_NAMED_THING: SPOKE_ANY_TYPE
    # missing
    # : SPOKE_LABEL_ANATOMY_CELL_TYPE
    # : SPOKE_LABEL_PHARMACOLOGIC_CLASS,
    # : SPOKE_LABEL_SIDE_EFFECT
}

SPOKE_BIOLINK_NODE_MAPPINGS = {
    SPOKE_LABEL_ANATOMY: BIOLINK_ENTITY_GROSS_ANATOMICAL_STRUCTURE,
    SPOKE_LABEL_ANATOMY_CELL_TYPE: BIOLINK_ENTITY_NAMED_THING,
    SPOKE_LABEL_BIOLOGICAL_PROCESS: BIOLINK_ENTITY_BIOLOGICAL_PROCESS,
    SPOKE_LABEL_CELL_TYPE: BIOLINK_ENTITY_CELL,
    SPOKE_LABEL_CELLULAR_COMPONENT: BIOLINK_ENTITY_CELLULAR_COMPONENT,
    SPOKE_LABEL_COMPOUND: BIOLINK_ENTITY_CHEMICAL_SUBSTANCE,
    SPOKE_LABEL_DISEASE: BIOLINK_ENTITY_DISEASE,
    SPOKE_LABEL_EC: BIOLINK_ENTITY_MOLECULAR_ACTIVITY,
    SPOKE_LABEL_FOOD: BIOLINK_ENTITY_FOOD,
    SPOKE_LABEL_GENE: BIOLINK_ENTITY_GENE,
    SPOKE_LABEL_MOLECULAR_FUNCTION: BIOLINK_ENTITY_MOLECULAR_ACTIVITY,
    SPOKE_LABEL_NUTRIENT: BIOLINK_ENTITY_NUTRIENT,
    SPOKE_LABEL_ORGANISM: BIOLINK_ENTITY_ORGANISM_TAXON,
    SPOKE_LABEL_PATHWAY: BIOLINK_ENTITY_PATHWAY,
    SPOKE_LABEL_PHARMACOLOGIC_CLASS: BIOLINK_ENTITY_NAMED_THING,
    SPOKE_LABEL_PROTEIN: BIOLINK_ENTITY_PROTEIN,
    SPOKE_LABEL_REACTION: BIOLINK_ENTITY_MOLECULAR_ACTIVITY,
    SPOKE_LABEL_SARSCOV2: BIOLINK_ENTITY_PROTEIN,
    SPOKE_LABEL_SIDE_EFFECT: BIOLINK_ENTITY_NAMED_THING,
    SPOKE_LABEL_SYMPTOM: BIOLINK_ENTITY_PHENOTYPIC_FEATURE,
}

# Edges
SPOKE_EDGE_TYPE_AFFECTS_CamG = 'AFFECTS_CamG'
SPOKE_EDGE_TYPE_ASSOCIATES_DaG = 'ASSOCIATES_DaG'
SPOKE_EDGE_TYPE_BINDS_CbP = 'BINDS_CbP'
SPOKE_EDGE_TYPE_CATALYZES_ECcR = 'CATALYZES_ECcR'
SPOKE_EDGE_TYPE_CAUSES_CcSE = 'CAUSES_CcSE'
SPOKE_EDGE_TYPE_CONSUMES_RcC = 'CONSUMES_RcC'
SPOKE_EDGE_TYPE_CONTAINS_AcA = 'CONTAINS_AcA'
SPOKE_EDGE_TYPE_CONTAINS_DcD = 'CONTAINS_DcD'
SPOKE_EDGE_TYPE_CONTAINS_FcC = 'CONTAINS_FcC'
SPOKE_EDGE_TYPE_CONTAINS_FcN = 'CONTAINS_FcN'
SPOKE_EDGE_TYPE_CONTAINS_OcO = 'CONTAINS_OcO'
SPOKE_EDGE_TYPE_CONTAINS_PWcPW = 'CONTAINS_PWcPW'
SPOKE_EDGE_TYPE_CONTRAINDICATES_CcD = 'CONTRAINDICATES_CcD'
SPOKE_EDGE_TYPE_DOWNREGULATES_AdG = 'DOWNREGULATES_AdG'
SPOKE_EDGE_TYPE_DOWNREGULATES_CdG = 'DOWNREGULATES_CdG'
SPOKE_EDGE_TYPE_DOWNREGULATES_GPdG = 'DOWNREGULATES_GPdG'
SPOKE_EDGE_TYPE_DOWNREGULATES_KGdG = 'DOWNREGULATES_KGdG'
SPOKE_EDGE_TYPE_DOWNREGULATES_OGdG = 'DOWNREGULATES_OGdG'
SPOKE_EDGE_TYPE_ENCODES_GeP = 'ENCODES_GeP'
SPOKE_EDGE_TYPE_ENCODES_OeP = 'ENCODES_OeP'
SPOKE_EDGE_TYPE_EXPRESSES_ACTeG = 'EXPRESSES_ACTeG'
SPOKE_EDGE_TYPE_EXPRESSES_AeG = 'EXPRESSES_AeG'
SPOKE_EDGE_TYPE_INCLUDES_OiEC = 'INCLUDES_OiEC'
SPOKE_EDGE_TYPE_INCLUDES_OiPW = 'INCLUDES_OiPW'
SPOKE_EDGE_TYPE_INCLUDES_PCiC = 'INCLUDES_PCiC'
SPOKE_EDGE_TYPE_INCLUDES_PWiEC = 'INCLUDES_PWiEC'
SPOKE_EDGE_TYPE_INTERACTS_CPiP = 'INTERACTS_CPiP'
SPOKE_EDGE_TYPE_INTERACTS_PiP = 'INTERACTS_PiP'
SPOKE_EDGE_TYPE_ISA_AiA = 'ISA_AiA'
SPOKE_EDGE_TYPE_ISA_DiD = 'ISA_DiD'
SPOKE_EDGE_TYPE_ISA_OiO = 'ISA_OiO'
SPOKE_EDGE_TYPE_ISA_PWiPW = 'ISA_PWiPW'
SPOKE_EDGE_TYPE_ISA_PiEC = 'ISA_PiEC'
SPOKE_EDGE_TYPE_ISIN_ACTiiA = 'ISIN_ACTiiA'
SPOKE_EDGE_TYPE_ISIN_ACTiiCT = 'ISIN_ACTiiCT'
SPOKE_EDGE_TYPE_LOCALIZES_DlA = 'LOCALIZES_DlA'
SPOKE_EDGE_TYPE_PARTICIPATES_GpBP = 'PARTICIPATES_GpBP'
SPOKE_EDGE_TYPE_PARTICIPATES_GpCC = 'PARTICIPATES_GpCC'
SPOKE_EDGE_TYPE_PARTICIPATES_GpMF = 'PARTICIPATES_GpMF'
SPOKE_EDGE_TYPE_PARTOF_ApA = 'PARTOF_ApA'
SPOKE_EDGE_TYPE_PRESENTS_DpS = 'PRESENTS_DpS'
SPOKE_EDGE_TYPE_PRODUCES_RpC = 'PRODUCES_RpC'
SPOKE_EDGE_TYPE_RESEMBLES_DrD = 'RESEMBLES_DrD'
SPOKE_EDGE_TYPE_TREATS_CtD = 'TREATS_CtD'
SPOKE_EDGE_TYPE_UPREGULATES_AuG = 'UPREGULATES_AuG'
SPOKE_EDGE_TYPE_UPREGULATES_CuG = 'UPREGULATES_CuG'
SPOKE_EDGE_TYPE_UPREGULATES_GPuG = 'UPREGULATES_GPuG'
SPOKE_EDGE_TYPE_UPREGULATES_KGuG = 'UPREGULATES_KGuG'
SPOKE_EDGE_TYPE_UPREGULATES_OGuG = 'UPREGULATES_OGuG'
# multi-omics temp
SPOKE_EDGE_TYPE_ASSOCIATES_DECREASEDRISK_CaD = 'ASSOCIATESDECREASEDRISK_CaD'
SPOKE_EDGE_TYPE_ASSOCIATES_INCREASEDRISK_CaD = 'ASSOCIATESINCREASEDRISK_CaD'
SPOKE_EDGE_TYPE_ASSOCIATES_DECREASEDRISK_DaD = 'ASSOCIATESDECREASEDRISK_DaD'
SPOKE_EDGE_TYPE_ASSOCIATES_INCREASEDRISK_DaD = 'ASSOCIATESINCREASEDRISK_DaD'
SPOKE_EDGE_TYPE_ASSOCIATES_RISK_DaD = 'ASSOCIATESRISK_DaD'


BIOLINK_ASSOCIATION_ASSOCIATED_WITH_RISK_FOR = 'biolink:associated_with_risk_for'
BIOLINK_ASSOCIATION_ASSOCIATED_WITH_DECREASED_RISK_FOR = 'biolink:associated_with_decreased_risk_for'
BIOLINK_ASSOCIATION_ASSOCIATED_WITH_INCREASED_RISK_FOR = 'biolink:associated_with_increased_risk_for'
BIOLINK_ASSOCIATION_CAUSES = 'biolink:causes'
BIOLINK_ASSOCIATION_CONDITION_ASSOCIATED_WITH_GENE = 'biolink:condition_associated_with_gene'
BIOLINK_ASSOCIATION_CONTRAINDICATED_FOR = 'biolink:contraindicated_for'
BIOLINK_ASSOCIATION_ENABLES = 'biolink:enables'
BIOLINK_ASSOCIATION_EXPRESSES = 'biolink:expresses'
BIOLINK_ASSOCIATION_HAS_GENE_PRODUCT = 'biolink:has_gene_product'
BIOLINK_ASSOCIATION_HAS_INPUT = 'biolink:has_input'
BIOLINK_ASSOCIATION_HAS_OUTPUT = 'biolink:has_output'
BIOLINK_ASSOCIATION_HAS_PART = 'biolink:has_part'
BIOLINK_ASSOCIATION_HAS_PHENOTYPE = 'biolink:has_phenotype'
BIOLINK_ASSOCIATION_INTERACTS_WITH = 'biolink:interacts_with'
BIOLINK_ASSOCIATION_MOLECULARLY_INTERACTS_WITH = 'biolink:molecularly_interacts_with'
BIOLINK_ASSOCIATION_NEGATIVELY_REGULATES_ENTITY_TO_ENTITY = 'biolink:negatively_regulates_entity_to_entity'
BIOLINK_ASSOCIATION_PART_OF = 'biolink:part_of'
BIOLINK_ASSOCIATION_PARTICIPATES_IN = 'biolink:participates_in'
BIOLINK_ASSOCIATION_POSITIVELY_REGULATES_ENTITY_TO_ENTITY = 'biolink:positively_regulates_entity_to_entity'
BIOLINK_ASSOCIATION_REGULATES_PROCESS_TO_PROCESS = 'biolink:regulates_process_to_process'
BIOLINK_ASSOCIATION_RELATED_TO = 'biolink:related_to'
BIOLINK_ASSOCIATION_SIMILAR_TO = 'biolink:similar_to'
BIOLINK_ASSOCIATION_SUBCLASS_OF = 'biolink:subclass_of'
BIOLINK_ASSOCIATION_TREATS = 'biolink:treats'

SPOKE_BIOLINK_EDGE_MAPPINGS = {
    SPOKE_EDGE_TYPE_ASSOCIATES_DECREASEDRISK_CaD : {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_ASSOCIATED_WITH_DECREASED_RISK_FOR,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003308'
    },
    SPOKE_EDGE_TYPE_ASSOCIATES_INCREASEDRISK_CaD: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_ASSOCIATED_WITH_INCREASED_RISK_FOR,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003308'
    },
    SPOKE_EDGE_TYPE_ASSOCIATES_DECREASEDRISK_DaD: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_ASSOCIATED_WITH_DECREASED_RISK_FOR,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003308'
    },
    SPOKE_EDGE_TYPE_ASSOCIATES_INCREASEDRISK_DaD: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_ASSOCIATED_WITH_INCREASED_RISK_FOR,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003308'
    },
    SPOKE_EDGE_TYPE_ASSOCIATES_RISK_DaD: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_ASSOCIATED_WITH_RISK_FOR,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003308'
    },
    SPOKE_EDGE_TYPE_AFFECTS_CamG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_REGULATES_PROCESS_TO_PROCESS,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002211'
    },
    SPOKE_EDGE_TYPE_ASSOCIATES_DaG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_CONDITION_ASSOCIATED_WITH_GENE,
        RELATIONSHIP_ONTOLOGY_CURIE: 'NCIT:R176'
    },
    SPOKE_EDGE_TYPE_BINDS_CbP: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_MOLECULARLY_INTERACTS_WITH,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002436'
    },
    SPOKE_EDGE_TYPE_CATALYZES_ECcR: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_ENABLES,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002327'
    },
    SPOKE_EDGE_TYPE_CAUSES_CcSE: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_CAUSES,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003303'
    },
    SPOKE_EDGE_TYPE_CONSUMES_RcC: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_INPUT,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002233'
    },
    SPOKE_EDGE_TYPE_CONTAINS_AcA: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_PART,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0001019'
    },
    SPOKE_EDGE_TYPE_CONTAINS_DcD: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_PART,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0001019'
    },
    SPOKE_EDGE_TYPE_CONTAINS_FcC: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_PART,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0001019'
    },
    SPOKE_EDGE_TYPE_CONTAINS_FcN: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_PART,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0001019'
    },
    SPOKE_EDGE_TYPE_CONTAINS_OcO: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_PART,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0001019'
    },
    SPOKE_EDGE_TYPE_CONTAINS_PWcPW: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_PART,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0001019'
    },
    SPOKE_EDGE_TYPE_CONTRAINDICATES_CcD: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_CONTRAINDICATED_FOR,
        RELATIONSHIP_ONTOLOGY_CURIE: 'DrugCentral:0000001'
    },
    SPOKE_EDGE_TYPE_DOWNREGULATES_AdG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_NEGATIVELY_REGULATES_ENTITY_TO_ENTITY,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003002'
    },
    SPOKE_EDGE_TYPE_DOWNREGULATES_CdG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_NEGATIVELY_REGULATES_ENTITY_TO_ENTITY,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003002'
    },
    SPOKE_EDGE_TYPE_DOWNREGULATES_GPdG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_NEGATIVELY_REGULATES_ENTITY_TO_ENTITY,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003002'
    },
    SPOKE_EDGE_TYPE_DOWNREGULATES_KGdG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_NEGATIVELY_REGULATES_ENTITY_TO_ENTITY,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003002'
    },
    SPOKE_EDGE_TYPE_DOWNREGULATES_OGdG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_NEGATIVELY_REGULATES_ENTITY_TO_ENTITY,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003002'
    },
    SPOKE_EDGE_TYPE_ENCODES_GeP: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_GENE_PRODUCT,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002205'
    },
    SPOKE_EDGE_TYPE_ENCODES_OeP: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_PART,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0001019'
    },
    SPOKE_EDGE_TYPE_EXPRESSES_ACTeG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_EXPRESSES,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002292'
    },
    SPOKE_EDGE_TYPE_EXPRESSES_AeG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_EXPRESSES,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002292'
    },
    SPOKE_EDGE_TYPE_INCLUDES_OiEC: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_PART,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002351'
    },
    SPOKE_EDGE_TYPE_INCLUDES_OiPW: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_PART,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002351'
    },
    SPOKE_EDGE_TYPE_INCLUDES_PCiC: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_PART,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002351'
    },
    SPOKE_EDGE_TYPE_INCLUDES_PWiEC: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_PART,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002351'
    },
    SPOKE_EDGE_TYPE_INTERACTS_CPiP: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_INTERACTS_WITH,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002434'
    },
    SPOKE_EDGE_TYPE_INTERACTS_PiP: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_INTERACTS_WITH,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002434'
    },
    SPOKE_EDGE_TYPE_ISA_AiA: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_PART_OF,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0001018'
    },
    SPOKE_EDGE_TYPE_ISA_DiD: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_SUBCLASS_OF,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0001018'
    },
    SPOKE_EDGE_TYPE_ISA_OiO: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_PART_OF,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0001018'
    },
    SPOKE_EDGE_TYPE_ISA_PiEC: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_RELATED_TO,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0000085'
    },
    SPOKE_EDGE_TYPE_ISA_PWiPW: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_PART_OF,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0001018'
    },
    SPOKE_EDGE_TYPE_ISIN_ACTiiA: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_PART_OF,
        RELATIONSHIP_ONTOLOGY_CURIE: 'BFO:0000050'
    },
    SPOKE_EDGE_TYPE_ISIN_ACTiiCT: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_PART_OF,
        RELATIONSHIP_ONTOLOGY_CURIE: 'BFO:0000050'
    },
    SPOKE_EDGE_TYPE_LOCALIZES_DlA: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_RELATED_TO,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0004026'
    },
    SPOKE_EDGE_TYPE_PARTICIPATES_GpBP: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_PARTICIPATES_IN,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0000056'
    },
    SPOKE_EDGE_TYPE_PARTICIPATES_GpCC: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_PARTICIPATES_IN,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0000056'
    },
    SPOKE_EDGE_TYPE_PARTICIPATES_GpMF: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_PARTICIPATES_IN,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0000056'
    },
    SPOKE_EDGE_TYPE_PARTOF_ApA: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_PART_OF,
        RELATIONSHIP_ONTOLOGY_CURIE: 'BFO:0000050'
    },
    SPOKE_EDGE_TYPE_PRESENTS_DpS: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_PHENOTYPE,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002452'
    },
    SPOKE_EDGE_TYPE_PRODUCES_RpC: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_HAS_OUTPUT,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002234'
    },
    SPOKE_EDGE_TYPE_RESEMBLES_DrD: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_SIMILAR_TO,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:HOM0000000'
    },
    SPOKE_EDGE_TYPE_TREATS_CtD: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_TREATS,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0002606'
    },
    SPOKE_EDGE_TYPE_UPREGULATES_AuG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_POSITIVELY_REGULATES_ENTITY_TO_ENTITY,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003003'
    },
    SPOKE_EDGE_TYPE_UPREGULATES_CuG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_POSITIVELY_REGULATES_ENTITY_TO_ENTITY,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003003'
    },
    SPOKE_EDGE_TYPE_UPREGULATES_GPuG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_POSITIVELY_REGULATES_ENTITY_TO_ENTITY,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003003'
    },
    SPOKE_EDGE_TYPE_UPREGULATES_KGuG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_POSITIVELY_REGULATES_ENTITY_TO_ENTITY,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003003'
    },
    SPOKE_EDGE_TYPE_UPREGULATES_OGuG: {
        BIOLINK_ASSOCIATION_TYPE: BIOLINK_ASSOCIATION_POSITIVELY_REGULATES_ENTITY_TO_ENTITY,
        RELATIONSHIP_ONTOLOGY_CURIE: 'RO:0003003'
    }
}

PREDICATES = {
    # SPOKE_LABEL_ANATOMY_CELL_TYPE: {
    #     BIOLINK_ENTITY_CELL: {
    #         BIOLINK_ASSOCIATION_PART_OF: SPOKE_EDGE_TYPE_ISIN_ACTiiCT
    #     },
    #     BIOLINK_ENTITY_GENE: {
    #         BIOLINK_ASSOCIATION_EXPRESSES: SPOKE_EDGE_TYPE_EXPRESSES_ACTeG
    #     },
    #     BIOLINK_ENTITY_GROSS_ANATOMICAL_STRUCTURE: {
    #         BIOLINK_ASSOCIATION_PART_OF: SPOKE_EDGE_TYPE_ISIN_ACTiiA
    #     }
    # },
    BIOLINK_ENTITY_CHEMICAL_SUBSTANCE: {
        BIOLINK_ENTITY_DISEASE: {
            BIOLINK_ASSOCIATION_ASSOCIATED_WITH_DECREASED_RISK_FOR: [SPOKE_EDGE_TYPE_ASSOCIATES_DECREASEDRISK_CaD],
            BIOLINK_ASSOCIATION_ASSOCIATED_WITH_INCREASED_RISK_FOR: [SPOKE_EDGE_TYPE_ASSOCIATES_INCREASEDRISK_CaD],
            BIOLINK_ASSOCIATION_CONTRAINDICATED_FOR: [SPOKE_EDGE_TYPE_CONTRAINDICATES_CcD],
            BIOLINK_ASSOCIATION_TREATS: [SPOKE_EDGE_TYPE_TREATS_CtD],
        },
        BIOLINK_ENTITY_GENE: {
            BIOLINK_ASSOCIATION_NEGATIVELY_REGULATES_ENTITY_TO_ENTITY: [SPOKE_EDGE_TYPE_DOWNREGULATES_CdG],
            BIOLINK_ASSOCIATION_POSITIVELY_REGULATES_ENTITY_TO_ENTITY: [SPOKE_EDGE_TYPE_UPREGULATES_CuG],
            BIOLINK_ASSOCIATION_REGULATES_PROCESS_TO_PROCESS: [SPOKE_EDGE_TYPE_AFFECTS_CamG]
        },
        BIOLINK_ENTITY_NAMED_THING: {  # SIDE EFFECT
            BIOLINK_ASSOCIATION_CAUSES: [SPOKE_EDGE_TYPE_CAUSES_CcSE]
        },
        BIOLINK_ENTITY_PROTEIN: {
            BIOLINK_ASSOCIATION_MOLECULARLY_INTERACTS_WITH: [SPOKE_EDGE_TYPE_BINDS_CbP]
        }
    },
    BIOLINK_ENTITY_DISEASE: {
        BIOLINK_ENTITY_DISEASE: {
            BIOLINK_ASSOCIATION_ASSOCIATED_WITH_RISK_FOR: [SPOKE_EDGE_TYPE_ASSOCIATES_RISK_DaD],
            BIOLINK_ASSOCIATION_ASSOCIATED_WITH_DECREASED_RISK_FOR: [SPOKE_EDGE_TYPE_ASSOCIATES_DECREASEDRISK_DaD],
            BIOLINK_ASSOCIATION_ASSOCIATED_WITH_INCREASED_RISK_FOR: [SPOKE_EDGE_TYPE_ASSOCIATES_INCREASEDRISK_DaD],
            BIOLINK_ASSOCIATION_HAS_PART: [SPOKE_EDGE_TYPE_CONTAINS_DcD],
            BIOLINK_ASSOCIATION_SUBCLASS_OF: [SPOKE_EDGE_TYPE_ISA_DiD],
            BIOLINK_ASSOCIATION_SIMILAR_TO: [SPOKE_EDGE_TYPE_RESEMBLES_DrD]
        },
        BIOLINK_ENTITY_GENE: {
            BIOLINK_ASSOCIATION_CONDITION_ASSOCIATED_WITH_GENE: [SPOKE_EDGE_TYPE_ASSOCIATES_DaG]
        },
        BIOLINK_ENTITY_GROSS_ANATOMICAL_STRUCTURE: {
            BIOLINK_ASSOCIATION_RELATED_TO: [SPOKE_EDGE_TYPE_LOCALIZES_DlA]
        },
        BIOLINK_ENTITY_PHENOTYPIC_FEATURE: {
            BIOLINK_ASSOCIATION_HAS_PHENOTYPE: [SPOKE_EDGE_TYPE_PRESENTS_DpS]
        }
    },
    BIOLINK_ENTITY_FOOD: {
        BIOLINK_ENTITY_CHEMICAL_SUBSTANCE: {
            BIOLINK_ASSOCIATION_HAS_PART: [SPOKE_EDGE_TYPE_CONTAINS_FcC]
        },
        BIOLINK_ENTITY_NUTRIENT: {
            BIOLINK_ASSOCIATION_HAS_PART: [SPOKE_EDGE_TYPE_CONTAINS_FcN]
        }
    },
    BIOLINK_ENTITY_GENE: {
        BIOLINK_ENTITY_BIOLOGICAL_PROCESS: {
            BIOLINK_ASSOCIATION_PARTICIPATES_IN: [SPOKE_EDGE_TYPE_PARTICIPATES_GpBP]
        },
        BIOLINK_ENTITY_CELLULAR_COMPONENT: {
            BIOLINK_ASSOCIATION_PARTICIPATES_IN: [SPOKE_EDGE_TYPE_PARTICIPATES_GpCC]
        },
        BIOLINK_ENTITY_GENE: {
            BIOLINK_ASSOCIATION_NEGATIVELY_REGULATES_ENTITY_TO_ENTITY: [
                SPOKE_EDGE_TYPE_DOWNREGULATES_GPdG,
                SPOKE_EDGE_TYPE_DOWNREGULATES_KGdG,
                SPOKE_EDGE_TYPE_DOWNREGULATES_OGdG
            ],
            BIOLINK_ASSOCIATION_POSITIVELY_REGULATES_ENTITY_TO_ENTITY: [
                SPOKE_EDGE_TYPE_UPREGULATES_GPuG,
                SPOKE_EDGE_TYPE_UPREGULATES_KGuG,
                SPOKE_EDGE_TYPE_UPREGULATES_OGuG
            ]
        },
        BIOLINK_ENTITY_MOLECULAR_ACTIVITY: {
            BIOLINK_ASSOCIATION_PARTICIPATES_IN: [SPOKE_EDGE_TYPE_PARTICIPATES_GpMF]
        },
        # BIOLINK_ENTITY_PATHWAY: {BIOLINK_ASSOCIATION_PARTICIPATES_IN:, Gene-participates-Pathway – see the first set of Pathway sources
        BIOLINK_ENTITY_PROTEIN: {
            BIOLINK_ASSOCIATION_HAS_GENE_PRODUCT: [SPOKE_EDGE_TYPE_ENCODES_GeP]
        },
    },
    BIOLINK_ENTITY_GROSS_ANATOMICAL_STRUCTURE: {
        BIOLINK_ENTITY_GROSS_ANATOMICAL_STRUCTURE: {
            BIOLINK_ASSOCIATION_HAS_PART: [SPOKE_EDGE_TYPE_CONTAINS_AcA],
            BIOLINK_ASSOCIATION_PART_OF: [SPOKE_EDGE_TYPE_ISA_AiA]
        },
        BIOLINK_ENTITY_GENE: {
            BIOLINK_ASSOCIATION_EXPRESSES: [SPOKE_EDGE_TYPE_EXPRESSES_AeG],
            BIOLINK_ASSOCIATION_NEGATIVELY_REGULATES_ENTITY_TO_ENTITY: [SPOKE_EDGE_TYPE_DOWNREGULATES_AdG],
            BIOLINK_ASSOCIATION_POSITIVELY_REGULATES_ENTITY_TO_ENTITY: [SPOKE_EDGE_TYPE_UPREGULATES_AuG],
        }
    },
    BIOLINK_ENTITY_MOLECULAR_ACTIVITY: {
        BIOLINK_ENTITY_CHEMICAL_SUBSTANCE: {
            BIOLINK_ASSOCIATION_HAS_INPUT: [SPOKE_EDGE_TYPE_CONSUMES_RcC],
            BIOLINK_ASSOCIATION_HAS_OUTPUT: [SPOKE_EDGE_TYPE_PRODUCES_RpC]
        },
        BIOLINK_ENTITY_MOLECULAR_ACTIVITY: {
            BIOLINK_ASSOCIATION_ENABLES: [SPOKE_EDGE_TYPE_CATALYZES_ECcR]
        }
    },
    BIOLINK_ENTITY_ORGANISM_TAXON: {
        # BIOLINK_ENTITY_DISEASE: {}  Organism-causes-Disease – from PathoPhenoDB,
        # currently just between organism SARS-CoV-2 and disease Covid-19
        BIOLINK_ENTITY_ORGANISM_TAXON: {
            BIOLINK_ASSOCIATION_PART_OF: [
                SPOKE_EDGE_TYPE_CONTAINS_OcO,
                SPOKE_EDGE_TYPE_ISA_OiO
            ]
        },
        BIOLINK_ENTITY_MOLECULAR_ACTIVITY: {
            BIOLINK_ASSOCIATION_HAS_PART: [SPOKE_EDGE_TYPE_INCLUDES_OiPW]
        },
        BIOLINK_ENTITY_PROTEIN: {
            BIOLINK_ASSOCIATION_HAS_PART: [SPOKE_EDGE_TYPE_ENCODES_OeP]  # TODO: check this
        },
        BIOLINK_ENTITY_PATHWAY: {
            BIOLINK_ASSOCIATION_HAS_PART: [SPOKE_EDGE_TYPE_INCLUDES_OiPW]
        }
    },
    BIOLINK_ENTITY_PATHWAY: {
        BIOLINK_ENTITY_MOLECULAR_ACTIVITY: {
            BIOLINK_ASSOCIATION_HAS_PART: [SPOKE_EDGE_TYPE_INCLUDES_PWiEC]
        },
        BIOLINK_ENTITY_PATHWAY: {
            BIOLINK_ASSOCIATION_HAS_PART: [SPOKE_EDGE_TYPE_CONTAINS_PWcPW],
            BIOLINK_ASSOCIATION_PART_OF: [SPOKE_EDGE_TYPE_ISA_PWiPW]
        }
    },
    # SPOKE_LABEL_PHARMACOLOGIC_CLASS: {
    #     BIOLINK_ENTITY_CHEMICAL_SUBSTANCE: [
    #         BIOLINK_ASSOCIATION_HAS_PART
    #     ]
    # }
    BIOLINK_ENTITY_PROTEIN: {
        # BIOLINK_ENTITY_DISEASE: [
        #     • Protein-decreasedin-Disease – from Institute for Systems Biology,
        #       human proteins decreased in Covid-19 disease (Su et al., 2020)
        #     • Protein-increasedin-Disease – from Institute for Systems Biology,
        #       human proteins increased in Covid-19 disease (Su et al., 2020)
        # ]
        BIOLINK_ENTITY_MOLECULAR_ACTIVITY: {
            BIOLINK_ASSOCIATION_RELATED_TO: [SPOKE_EDGE_TYPE_ISA_PiEC]
        },
        BIOLINK_ENTITY_PROTEIN: {
            BIOLINK_ASSOCIATION_INTERACTS_WITH: [
                SPOKE_EDGE_TYPE_INTERACTS_CPiP, SPOKE_EDGE_TYPE_INTERACTS_PiP
            ]
        }
    },
    # SPOKE_LABEL_PROTEIN_DOMAIN: {
    #     • ProteinDomain-memberof-ProteinFamily – from Pfam
    #     • ProteinDomain-partof-Protein – from InterPro
    # }
}

BIOLINK_SPOKE_EDGE_MAPPINGS = defaultdict(list)
for biolink_subject, biolink_object_map in PREDICATES.items():
    for biolink_object, predicates_map in biolink_object_map.items():
        for predicate, spoke_edge_type in predicates_map.items():
            BIOLINK_SPOKE_EDGE_MAPPINGS[predicate].extend(spoke_edge_type)
